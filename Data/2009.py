from pybaseball import cache
cache.enable()

from pybaseball import batting_stats
import pandas as pd

players_2009 = batting_stats(2009, qual=200)
print("Data pulled successfully")

columns = [
    "Name", "Team", "Age", "PA",
    "OBP", "SLG", "OPS",
    "wOBA", "ISO",
    "BB%", "K%",
    "HR", "RBI", "SB",
    "Def", "WAR"
]

columns = [c for c in columns if c in players_2009.columns]

final_df = players_2009.loc[:, columns].dropna().copy()

final_df["All_Star"] = 0
final_df["Year"] = 2009

all_stars_2009_hitters = [
    # AL
    "Joe Mauer", "Victor Martinez", "Justin Morneau", "Mark Teixeira",
    "Dustin Pedroia", "Evan Longoria", "Derek Jeter", "Jason Bartlett",
    "Ichiro Suzuki", "Torii Hunter", "Josh Hamilton", "Carl Crawford",
    "Michael Young",

    # NL
    "Brian McCann", "Yadier Molina", "Albert Pujols", "Adrian Gonzalez",
    "Chase Utley", "David Wright", "Hanley Ramirez", "Jimmy Rollins",
    "Ryan Braun", "Matt Holliday", "Carlos Beltran", "Nate McLouth"
]

final_df.loc[
    final_df["Name"].isin(all_stars_2009_hitters),
    "All_Star"
] = 1

print(final_df.columns)
print(final_df["All_Star"].value_counts())

final_df.to_csv("mlb_2009_stats.csv", index=False)
print("CSV saved!")
