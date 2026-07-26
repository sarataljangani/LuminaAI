import os
import pandas as pd

from features.feature_extractor import extract_features

labels = pd.read_csv("data/competition_dataset/labels.csv")

dataset = []

for _, row in labels.iterrows():

    file_name = row["audio_file"]

    speaker = row["speaker_id"]

    path = os.path.join(
        "data/competition_dataset",
        file_name
    )

    features = extract_features(path)

    data = {
        "speaker_id": speaker
    }

    for i, value in enumerate(features):

        data[f"Feature_{i+1}"] = value

    dataset.append(data)

df = pd.DataFrame(dataset)

df.to_csv(
    "data/features.csv",
    index=False
)

print(df.head())

print()

print(df.shape)