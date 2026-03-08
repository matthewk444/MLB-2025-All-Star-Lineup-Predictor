from pybaseball import cache
cache.enable()

from pybaseball import batting_stats
import pandas as pd

players_2010 = batting_stats(2010, qual=200)
print("Data pulled successfully")

columns = [
    "Name", "Team", "Age", "PA",
    "OBP", "SLG", "OPS",
    "wOBA", "ISO",
    "BB%", "K%",
    "HR", "RBI", "SB",
    "Def", "WAR"
]

columns = [c for c in columns if c in players_2010.columns]

final_df = players_2010.loc[:, columns].dropna().copy()

final_df["All_Star"] = 0
final_df["Year"] = 2010

all_stars_2010_hitters = [
    # AL
    "Joe Mauer", "Victor Martinez", "Miguel Cabrera", "Mark Teixeira",
    "Robinson Cano", "Dustin Pedroia", "Evan Longoria", "Alex Rodriguez",
    "Derek Jeter", "Josh Hamilton", "Ichiro Suzuki", "Carl Crawford",
    "Vernon Wells", "Vladimir Guerrero",

    # NL
    "Yadier Molina", "Brian McCann", "Albert Pujols", "Ryan Howard",
    "Dan Uggla", "Chase Utley", "David Wright", "Hanley Ramirez",
    "Ryan Braun", "Matt Holliday", "Jason Heyward", "Corey Hart"
]


final_df.loc[
    final_df["Name"].isin(all_stars_2010_hitters),
    "All_Star"
] = 1

print(final_df.columns)
print(final_df["All_Star"].value_counts())

final_df.to_csv("mlb_2010_stats.csv", index=False)
print("CSV saved!")
