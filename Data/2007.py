from pybaseball import cache
cache.enable()

from pybaseball import batting_stats
import pandas as pd

players_2007 = batting_stats(2007, qual=200)
print("Data pulled successfully")

columns = [
    "Name","Year", "Team", "Age", "PA",
    "OBP", "SLG", "OPS",
    "wOBA", "ISO",
    "BB%", "K%",
    "HR", "RBI", "SB",
    "Def", "WAR"
]

# Keep only columns that exist
columns = [c for c in columns if c in players_2007.columns]

# 🔑 FORCE A REAL COPY HERE
final_df = players_2007.loc[:, columns].dropna().copy()

# 🔑 CREATE COLUMN ON THE REAL DF
final_df["All_Star"] = 0
final_df["Year"] = 2007

all_stars_2007_hitters = [
    "Ivan Rodriguez", "Victor Martinez", "Justin Morneau", "Carlos Pena",
    "Dustin Pedroia", "Alex Rodriguez", "Derek Jeter",
    "Ichiro Suzuki", "Magglio Ordonez", "Vladimir Guerrero",
    "Torii Hunter", "David Ortiz",
    "Russell Martin", "Brian McCann", "Prince Fielder", "Albert Pujols",
    "Chase Utley", "David Wright", "Jose Reyes",
    "Ken Griffey Jr.", "Carlos Beltran", "Matt Holliday", "Barry Bonds"
]

# 🔑 LABEL
final_df.loc[
    final_df["Name"].isin(all_stars_2007_hitters),
    "All_Star"
] = 1

# 🔍 PROVE IT EXISTS
print(final_df.columns)
print(final_df["All_Star"].value_counts())

final_df.to_csv("mlb_2007b_stats.csv", index=False)
print("CSV saved!")
