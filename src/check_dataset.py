import pandas as pd

df = pd.read_csv("data/features.csv")

print(df.info())

print("\n")

print(df.describe())

print("\n")

print(df["Person"].value_counts())