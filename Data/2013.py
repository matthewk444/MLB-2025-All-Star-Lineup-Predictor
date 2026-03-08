from pybaseball import cache
cache.enable()

from pybaseball import batting_stats
import pandas as pd

players_2013 = batting_stats(2013, qual=200)
print("Data pulled successfully")

columns = [
    "Name", "Team", "Age", "PA",
    "OBP", "SLG", "OPS",
    "wOBA", "ISO",
    "BB%", "K%",
    "HR", "RBI", "SB",
    "Def", "WAR"
]

columns = [c for c in columns if c in players_2013.columns]

final_df = players_2013.loc[:, columns].dropna().copy()

final_df["All_Star"] = 0
final_df["Year"] = 2013

all_stars_2013_batters = [
    # American League
    "Joe Mauer",
    "Chris Davis",
    "Robinson Cano",
    "Manny Machado",
    "Jhonny Peralta",
    "Mike Trout",
    "Adam Jones",
    "David Ortiz",

    # National League
    "Buster Posey",
    "Joey Votto",
    "Matt Carpenter",
    "David Wright",
    "Troy Tulowitzki",
    "Carlos Gomez",
    "Bryce Harper",
    "Carlos Gonzalez"
]





final_df.loc[
    final_df["Name"].isin(all_stars_2013_batters),
    "All_Star"
] = 1

print(final_df.columns)
print(final_df["All_Star"].value_counts())

final_df.to_csv("mlb_2013_stats.csv", index=False)
print("CSV saved!")
