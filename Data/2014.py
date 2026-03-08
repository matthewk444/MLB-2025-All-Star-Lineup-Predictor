from pybaseball import cache
cache.enable()

from pybaseball import batting_stats
import pandas as pd

players_2014 = batting_stats(2014, qual=200)
print("Data pulled successfully")

columns = [
    "Name", "Team", "Age", "PA",
    "OBP", "SLG", "OPS",
    "wOBA", "ISO",
    "BB%", "K%",
    "HR", "RBI", "SB",
    "Def", "WAR"
]

columns = [c for c in columns if c in players_2014.columns]

final_df = players_2014.loc[:, columns].dropna().copy()

final_df["All_Star"] = 0
final_df["Year"] = 2014

all_stars_2014_batters = [
    # American League
    "Matt Wieters",
    "Miguel Cabrera",
    "Robinson Cano",
    "Adrian Beltre",
    "Derek Jeter",
    "Mike Trout",
    "Adam Jones",
    "Jose Bautista",
    "Victor Martinez",

    # National League
    "Yadier Molina",
    "Paul Goldschmidt",
    "Chase Utley",
    "Aramis Ramirez",
    "Troy Tulowitzki",
    "Andrew McCutchen",
    "Carlos Gomez",
    "Giancarlo Stanton"
]






final_df.loc[
    final_df["Name"].isin(all_stars_2014_batters),
    "All_Star"
] = 1

print(final_df.columns)
print(final_df["All_Star"].value_counts())

final_df.to_csv("mlb_2014_stats.csv", index=False)
print("CSV saved!")
