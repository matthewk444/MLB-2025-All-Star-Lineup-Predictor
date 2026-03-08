import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report






#Load Datasets and Binary Classifier

data = pd.read_csv('Data/combined_output.csv')  

X_train = data.drop(columns = ["Name", "Team", "Age", "All_Star"])
Y_train = data["All_Star"]

#Scale All Features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

#Scale for Test
players_2025 = pd.read_csv('Data/mlb_2025_stats.csv')

X_test = players_2025.drop(columns = ["Name", "Team", "Age"])
X_test_scaled = scaler.transform(X_test)

#KNN Classifier
knn = KNeighborsClassifier(
    n_neighbors=5,
    metric="euclidean",
    weights="distance"
)


knn.fit(X_train_scaled, Y_train)

probs = knn.predict_proba(X_test_scaled)[:, 1]
players_2025["Predicted_All_Star"] = (probs >= 0.25).astype(int)



all_stars_2025_hitters = [
     "Cal Raleigh",
    "Vladimir Guerrero Jr.",
    "Gleyber Torres",
    "Riley Greene",
    "Aaron Judge",
    "Ryan O'Hearn",
    "Junior Caminero",
    "Javier Baez",
    "Jacob Wilson",

    # National League
    "Shohei Ohtani",
    "Ronald Acuna Jr.",
    "Ketel Marte",
    "Freddie Freeman",
    "Manny Machado",
    "Will Smith",
    "Kyle Tucker",
    "Francisco Lindor",
    "Pete Crow-Armstrong",

    # NL Reserves (Hitters)
    "Pete Alonso",
    "Brendan Donovan",
    "Kyle Schwarber",
    "Kyle Stowers",
    "Hunter Goodman"
]

players_2025["Actual_All_Star"] = 0
players_2025.loc[
    players_2025["Name"].isin(all_stars_2025_hitters),
    "Actual_All_Star"
] = 1







print(classification_report(
    players_2025["Actual_All_Star"],
    players_2025["Predicted_All_Star"]
))



