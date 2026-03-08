from pybaseball import cache
cache.enable()

from pybaseball import batting_stats
import pandas as pd

players_2011 = batting_stats(2011, qual=200)
print("Data pulled successfully")

columns = [
    "Name", "Team", "Age", "PA",
    "OBP", "SLG", "OPS",
    "wOBA", "ISO",
    "BB%", "K%",
    "HR", "RBI", "SB",
    "Def", "WAR"
]

columns = [c for c in columns if c in players_2011.columns]

final_df = players_2011.loc[:, columns].dropna().copy()

final_df["All_Star"] = 0
final_df["Year"] = 2011

all_stars_2011_hitters = [
    # AL
    "Alex Avila", "Matt Wieters", "Adrian Gonzalez", "Mark Teixeira",
    "Robinson Cano", "Dustin Pedroia", "Adrian Beltre", "Alex Rodriguez",
    "Derek Jeter", "Jose Bautista", "Josh Hamilton", "Curtis Granderson",
    "Jacoby Ellsbury", "David Ortiz",

    # NL
    "Brian McCann", "Yadier Molina", "Prince Fielder", "Ryan Howard",
    "Rickie Weeks", "Dan Uggla", "David Wright", "Troy Tulowitzki",
    "Matt Holliday", "Ryan Braun", "Justin Upton", "Shane Victorino"
]



final_df.loc[
    final_df["Name"].isin(all_stars_2011_hitters),
    "All_Star"
] = 1

print(final_df.columns)
print(final_df["All_Star"].value_counts())

final_df.to_csv("mlb_2011_stats.csv", index=False)
print("CSV saved!")
