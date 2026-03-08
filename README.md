# MLB-2025-All-Star-Lineup-Predictor
A machine learning model that predicts MLB All-Star selections using historical batting statistics.
The model is trained on player data from 2007–2014 and applied to 2025 MLB players to estimate their All-Star probability.


Project Overview

Selecting MLB All-Stars is highly competitive — only ~6% of qualified players make the team each year.
This project trains a Random Forest classifier on historical batting statistics to predict which players are most likely to receive an All-Star selection.

The model learns patterns from 2,784 player-seasons and applies them to modern players.

Key goals of this project:
	•	Build a classifier for rare-event prediction
	•	Handle class imbalance (94% non-All-Stars vs 6% All-Stars)
	•	Evaluate performance using cross-validation and held-out test data
	•	Analyze feature importance in All-Star selections

Metric
Value
Cross-Validation ROC-AUC
0.917 ± 0.030
Cross-Validation F1 (All-Stars)
0.502
2025 Test Precision
0.45
2025 Test Recall
0.57
2025 Test Accuracy
94%

The model performs well despite the extreme class imbalance.

Rank
Feature
Importance
1
WAR
0.226
2
OPS
0.123
3
RBI
0.119
4
wOBA
0.118
5
PA
0.094
6
SLG
0.088
7
OBP
0.067
8
ISO
0.032
9
Defensive Value
0.031
10
HR
0.031
Data Collection

Batting statistics were pulled using the pybaseball package.

Training dataset:
	•	Seasons: 2007–2014
	•	Minimum: ≥200 Plate Appearances
	•	Total observations: 2,784 player-seasons

All-Star labels were manually verified per season.


The final model uses:

RandomForestClassifier(
    n_estimators=300,
    max_depth=6,
    class_weight="balanced",
    random_state=42
)

Handling imbalance is critical since only 6% of players become All-Stars.

Threshold Optimization

Rather than using a default probability cutoff of 0.50, the decision threshold was tuned using the precision-recall curve.

Optimal threshold:≈ 0.499

Example 2025 Predictions

The model successfully identified several high-probability All-Stars:

Aaron Judge = 0.938
Ketel Marte = 0.830
Shohei Ohtani = 0.825

Some notable false negatives included:
	•	Ronald Acuña Jr. (0.495)
	•	Francisco Lindor (0.449)

These cases highlight the influence of reputation, fan voting, and narrative beyond pure statistics.

Baseball_project/
│
├── Data/
│   ├── combined_output.csv      # Training data (2007–2014)
│   └── mlb_2025_stats.csv       # 2025 player statistics
│
├── KNN/
│   └── classification.py        # Main model script
│
├── 2007.py – 2014.py            # Data collection scripts
├── 2025.py                      # 2025 data collection
└── README.md

⚙️ Dependencies
pandas
numpy
scikit-learn
pybaseball

Future Improvements

Possible extensions for the project:
	•	Add pitcher All-Star predictions
	•	Incorporate Statcast metrics
	•	Use XGBoost / Gradient Boosting
	•	Build a web dashboard for predictions
	•	Add visualizations of feature importance and ROC curves


Inspiration

This project explores how sabermetrics and machine learning can model real MLB award outcomes. While All-Star selections involve subjective factors (fan voting, reputation, team performance), statistical models can still capture much of the underlying signal.
