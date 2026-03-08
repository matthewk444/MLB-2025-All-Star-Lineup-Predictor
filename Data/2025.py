from pybaseball import cache
cache.enable()

from pybaseball import batting_stats
import pandas as pd

players_2025 = batting_stats(2025, qual=100)
print("Data pulled successfully")

df_players_2025 = players_2025.copy()

columns = [
    "Name", "Team", "Age", "PA",
    "OBP", "SLG", "OPS",
    "wOBA", "ISO",
    "BB%", "K%",
    "HR", "RBI", "SB",
    "Def", "WAR"
]

# Keep only columns that actually exist (prevents crashes)
columns = [c for c in columns if c in df_players_2025.columns]

final_df = df_players_2025[columns].dropna()
final_df["Year"] = 2025


final_df.to_csv("mlb_2025_stats.csv", index=False)
print("CSV saved!")
