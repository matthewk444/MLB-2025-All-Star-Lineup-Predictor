import pandas as pd

filepath1 = "Data/mlb_2007b_stats.csv"
filepath2 = "Data/mlb_2008_stats.csv"
filepath3 = "Data/mlb_2009_stats.csv"
filepath4 = "Data/mlb_2010_stats.csv"
filepath5 = "Data/mlb_2011_stats.csv"
filepath6 = "Data/mlb_2012_stats.csv"
filepath7 = "Data/mlb_2013_stats.csv"
filepath8 = "Data/mlb_2014_stats.csv"
output_path = 'combined_output.csv'

df1 = pd.read_csv(filepath1)
df2 = pd.read_csv(filepath2)
df3 = pd.read_csv(filepath3)
df4 = pd.read_csv(filepath4)
df5 = pd.read_csv(filepath5)
df6 = pd.read_csv(filepath6)
df7 = pd.read_csv(filepath7)
df8 = pd.read_csv(filepath8)

combined_df = pd.concat([ df1, df2, df3, df4, df5, df6, df7, df8], ignore_index=True)

combined_df.to_csv(output_path, index=False)
print(f"Combined CSV saved to {output_path}!")  
