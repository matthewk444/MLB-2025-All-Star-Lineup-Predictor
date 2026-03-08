from pybaseball import cache
cache.enable()

from pybaseball import batting_stats
import pandas as pd

players_2012 = batting_stats(2012, qual=200)
print("Data pulled successfully")

columns = [
    "Name", "Team", "Age", "PA",
    "OBP", "SLG", "OPS",
    "wOBA", "ISO",
    "BB%", "K%",
    "HR", "RBI", "SB",
    "Def", "WAR"
]

columns = [c for c in columns if c in players_2012.columns]

final_df = players_2012.loc[:, columns].dropna().copy()

final_df["All_Star"] = 0
final_df["Year"] = 2012

all_stars_2012_batters = [
    # American League
    "Joe Mauer",
    "Prince Fielder",
    "Robinson Cano",
    "Adrian Beltre",
    "Derek Jeter",
    "Josh Hamilton",
    "Curtis Granderson",
    "Mike Trout",
    "David Ortiz",

    # National League
    "Buster Posey",
    "Joey Votto",
    "Dan Uggla",
    "Pablo Sandoval",
    "Rafael Furcal",
    "Ryan Braun",
    "Carlos Beltran",
    "Giancarlo Stanton"
]




final_df.loc[
    final_df["Name"].isin(all_stars_2012_batters),
    "All_Star"
] = 1

print(final_df.columns)
print(final_df["All_Star"].value_counts())

final_df.to_csv("mlb_2012_stats.csv", index=False)
print("CSV saved!")
