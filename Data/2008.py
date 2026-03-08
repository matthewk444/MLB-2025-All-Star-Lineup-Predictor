from pybaseball import cache
cache.enable()

from pybaseball import batting_stats
import pandas as pd

players_2008 = batting_stats(2008, qual=200)
print("Data pulled successfully")

columns = [
    "Name", "Team", "Age", "PA",
    "OBP", "SLG", "OPS",
    "wOBA", "ISO",
    "BB%", "K%",
    "HR", "RBI", "SB",
    "Def", "WAR"
]

columns = [c for c in columns if c in players_2008.columns]

final_df = players_2008.loc[:, columns].dropna().copy()

final_df["All_Star"] = 0
final_df["Year"] = 2008


all_stars_2008_hitters = [
    # AL
    "Joe Mauer", "Jason Varitek", "Carlos Pena", "Justin Morneau",
    "Dustin Pedroia", "Alex Rodriguez", "Michael Young",
    "Ichiro Suzuki", "Josh Hamilton", "Manny Ramirez",
    "Torii Hunter", "Milton Bradley",

    # NL
    "Brian McCann", "Geovany Soto", "Albert Pujols", "Lance Berkman",
    "Chase Utley", "Chipper Jones", "Hanley Ramirez",
    "Ryan Braun", "Alfonso Soriano", "Carlos Beltran", "Matt Holliday"
]


final_df.loc[
    final_df["Name"].isin(all_stars_2008_hitters),
    "All_Star"
] = 1

# 🔍 PROVE IT EXISTS
print(final_df.columns)
print(final_df["All_Star"].value_counts())

final_df.to_csv("mlb_2008_stats.csv", index=False)
print("CSV saved!")
