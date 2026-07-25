import pandas as pd

df = pd.read_csv("data/features.csv")

<<<<<<< HEAD
print(df.info())

print("\n")

print(df.describe())

print("\n")

=======
print(df.head())

print()

print("Shape:")
print(df.shape)

print()

print("Columns:")
print(df.columns)

print()

print("Classes:")
>>>>>>> ec08a901f3cd2ab006c4ccf4a9df40ed1ab4dd79
print(df["Person"].value_counts())