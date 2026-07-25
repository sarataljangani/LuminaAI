import os
import pandas as pd

from features.feature_extractor import extract_features

base_path = "data/voices"

dataset = []

for person in os.listdir(base_path):

    person_folder = os.path.join(base_path, person)

    if not os.path.isdir(person_folder):
        continue

    for file in os.listdir(person_folder):

        if file.endswith(".wav"):

            path = os.path.join(person_folder, file)

            features = extract_features(path)

            row = {
                "Person": person
            }

            for i, value in enumerate(features):
                row[f"Feature_{i+1}"] = value

            dataset.append(row)

df = pd.DataFrame(dataset)

df.to_csv(
    "data/features.csv",
    index=False
)

print(df.head())

print()

print(df.shape)

print()

print(df.columns)