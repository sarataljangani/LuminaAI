import os
import pandas as pd

from features.feature_extractor import extract_features

labels = pd.read_csv("data/training/labels.csv")

dataset = []

for _, row in labels.iterrows():

    file_name = row["audio_file"]

    speaker = row["speaker_id"]

    path = os.path.join(
        "data/training",
        file_name
    )

    features = extract_features(path)

    sample = {
        "speaker_id": speaker
    }

    for i, value in enumerate(features):
        sample[f"Feature_{i+1}"] = value

    dataset.append(sample)

df = pd.DataFrame(dataset)

df.to_csv(
    "data/features.csv",
    index=False
)

print(df.head())

print(df.shape)