import pandas as pd

data = {
    "Name": ["Sara", "Saba", "Fatemeh", "Ali"],
    "Age": [22, 22, 22, 23],
    "Score": [19.5, 19.2, 18.9, 19.8]
}

df = pd.DataFrame(data)

print("DataFrame")
print(df)
print()

print("Head")
print(df.head())
print()

print("Tail")
print(df.tail())
print()

print("Shape")
print(df.shape)
print()

print("Describe")
print(df.describe())
print()

print("Info")
df.info()