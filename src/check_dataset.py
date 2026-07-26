import pandas as pd

df = pd.read_csv("data/features.csv")

print(df.head())

print()

print("Shape:")
print(df.shape)

print()

print("Columns:")
print(df.columns)

print()

print("Classes:")
print(df["Person"].value_counts())
 