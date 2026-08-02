import librosa

import numpy as np


def extract_features(audio, sr):
    """
    Extract MFCC features.

    Parameters
    ----------

    audio : np.ndarray

    sr : int

    Returns
    -------

    feature_vector : np.ndarray
    """

    mfcc = librosa.feature.mfcc(
        y=audio,
        sr=sr,
        n_mfcc=13
    )

    feature_vector = np.mean(
        mfcc,
        axis=1
    )

    return feature_vector