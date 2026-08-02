import os
import pandas as pd

from audio_loader import load_audio
from feature_extractor import extract_features


def create_dataset(
    labels_path,
    audio_folder,
    output_path
):
    """
    Build feature dataset from audio files.
    """

    pass
labels = pd.read_csv(labels_path)

print(labels.head())

dataset = []
{
    "speaker_id": 12,

    "mfcc_1": ...

    "mfcc_2": ...

    ...

    "mfcc_13": ...
}