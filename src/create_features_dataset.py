import logging
import os

import pandas as pd
from tqdm import tqdm

from audio_loader import load_audio
from feature_extractor import extract_features


# ==========================
# Logging Configuration
# ==========================

logging.basicConfig(
    filename="logs/feature_extraction.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)


# ==========================
# Dataset Builder
# ==========================

def create_dataset(
    labels_path,
    audio_folder,
    output_path
):
    """
    Create feature dataset from audio files.
    """

    # Read labels
    labels = pd.read_csv(labels_path)

    # Validate CSV columns
    required_columns = [
        "speaker_id",
        "audio_file"
    ]

    for column in required_columns:
        if column not in labels.columns:
            raise ValueError(f"Missing column: {column}")

    dataset = []

    # Process all audio files
    for _, row in tqdm(
        labels.iterrows(),
        total=len(labels),
        desc="Extracting Features"
    ):

        speaker_id = row["speaker_id"]
        audio_file = row["audio_file"]

        audio_path = os.path.join(
            audio_folder,
            audio_file
        )

        try:

            audio, sr = load_audio(audio_path)

            features = extract_features(
                audio,
                sr
            )

        except Exception as e:

            logging.error(
                f"{audio_file} : {e}"
            )

            print(f"Error processing {audio_file}")

            continue

        sample = {
            "speaker_id": speaker_id,
            "audio_file": audio_file
        }

        for i, value in enumerate(features):
            sample[f"mfcc_{i+1}"] = value

        dataset.append(sample)

    # Convert to DataFrame
    df = pd.DataFrame(dataset)

    # Save CSV
    df.to_csv(
        output_path,
        index=False
    )

    print(f"Processed {len(dataset)} files.")
    print("Dataset Created Successfully.")


# ==========================
# Main
# ==========================

if __name__ == "__main__":

    create_dataset(
        labels_path="data/training/labels.csv",
        audio_folder="data/training",
        output_path="data/features.csv"
    )
    