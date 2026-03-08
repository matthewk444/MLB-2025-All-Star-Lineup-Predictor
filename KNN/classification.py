import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold, cross_val_predict, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score, precision_recall_curve
import warnings
warnings.filterwarnings('ignore')

# ── 1. Load & prep training data ─────────────────────────────────────────────
data = pd.read_csv('Data/combined_output.csv')

FEATURE_COLS = ["PA", "OBP", "SLG", "OPS", "wOBA", "ISO",
                "BB%", "K%", "HR", "RBI", "SB", "Def", "WAR", "Year"]

X_train = data[FEATURE_COLS]
y_train = data["All_Star"]

print(f"Training data: {X_train.shape[0]} players | "
      f"All-Stars: {y_train.sum()} ({y_train.mean()*100:.1f}%)")

# ── 2. Scale features ────────────────────────────────────────────────────────
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# ── 3. Model: Random Forest with balanced class weights ──────────────────────
#   Why RF over KNN?
#   - KNN suffers badly with class imbalance (6% positive rate here)
#   - RF's class_weight='balanced' up-weights the rare All-Star class
#   - RF gives feature importances and probability calibration
rf = RandomForestClassifier(
    n_estimators=300,
    max_depth=6,
    min_samples_leaf=3,
    class_weight='balanced',   # key fix for imbalance
    random_state=42,
    n_jobs=-1
)

# ── 4. Cross-validated probability estimates (no data leakage) ───────────────
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
train_probs = cross_val_predict(rf, X_train_scaled, y_train,
                                cv=cv, method='predict_proba')[:, 1]

# ── 5. Find optimal decision threshold via F1 ────────────────────────────────
precision, recall, thresholds = precision_recall_curve(y_train, train_probs)
f1_scores = 2 * precision * recall / (precision + recall + 1e-9)
best_threshold = thresholds[np.argmax(f1_scores)]
print(f"\nOptimal threshold: {best_threshold:.3f}  (cross-validated F1: {f1_scores.max():.3f})")

# ── 6. Cross-val summary ─────────────────────────────────────────────────────
auc_scores = cross_val_score(rf, X_train_scaled, y_train, cv=cv, scoring='roc_auc')
print(f"Cross-val ROC-AUC: {auc_scores.mean():.3f} ± {auc_scores.std():.3f}")

train_preds = (train_probs >= best_threshold).astype(int)
print("\n── Training Cross-Val Report ──")
print(classification_report(y_train, train_preds))

# ── 7. Fit final model on all training data ──────────────────────────────────
rf.fit(X_train_scaled, y_train)

# Feature importance
importances = (pd.Series(rf.feature_importances_, index=FEATURE_COLS)
               .sort_values(ascending=False))
print("── Feature Importances ──")
print(importances.round(3).to_string())

# ── 8. Predict 2025 All-Stars ────────────────────────────────────────────────
players_2025 = pd.read_csv('Data/mlb_2025_stats.csv')

# Align features — add Year if missing
if "Year" not in players_2025.columns:
    players_2025["Year"] = 2025

X_test = players_2025[FEATURE_COLS]
X_test_scaled = scaler.transform(X_test)

test_probs = rf.predict_proba(X_test_scaled)[:, 1]
players_2025["AS_Probability"] = test_probs.round(3)
players_2025["Predicted_All_Star"] = (test_probs >= best_threshold).astype(int)

# ── 9. Ground truth for 2025 (if available) ──────────────────────────────────
all_stars_2025 = [
    # AL
    "Cal Raleigh", "Vladimir Guerrero Jr.", "Gleyber Torres",
    "Riley Greene", "Aaron Judge", "Ryan O'Hearn",
    "Junior Caminero", "Javier Baez", "Jacob Wilson",
    # NL
    "Shohei Ohtani", "Ronald Acuna Jr.", "Ketel Marte",
    "Freddie Freeman", "Manny Machado", "Will Smith",
    "Kyle Tucker", "Francisco Lindor", "Pete Crow-Armstrong",
    # NL Reserves
    "Pete Alonso", "Brendan Donovan", "Kyle Schwarber",
    "Kyle Stowers", "Hunter Goodman",
]

players_2025["Actual_All_Star"] = players_2025["Name"].isin(all_stars_2025).astype(int)

# ── 10. Results ───────────────────────────────────────────────────────────────
print("\n── 2025 Prediction Report ──")
print(classification_report(
    players_2025["Actual_All_Star"],
    players_2025["Predicted_All_Star"]
))

# Show predicted All-Stars ranked by probability
predicted = (players_2025[players_2025["Predicted_All_Star"] == 1]
             [["Name", "Team", "WAR", "OPS", "wOBA", "AS_Probability", "Actual_All_Star"]]
             .sort_values("AS_Probability", ascending=False))

print("\n── Predicted 2025 All-Stars (ranked by probability) ──")
print(predicted.to_string(index=False))

# Missed All-Stars (false negatives)
missed = players_2025[
    (players_2025["Actual_All_Star"] == 1) &
    (players_2025["Predicted_All_Star"] == 0)
][["Name", "Team", "WAR", "OPS", "AS_Probability"]]

if not missed.empty:
    print("\n── Missed All-Stars (false negatives) ──")
    print(missed.sort_values("AS_Probability", ascending=False).to_string(index=False))