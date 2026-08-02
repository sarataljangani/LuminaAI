import librosa


def load_audio(file_path):
    """
    Load audio file.

    Parameters
    ----------
    file_path : str
        Path to audio file.

    Returns
    -------
    audio : np.ndarray
        Audio samples.

    sr : int
        Sample rate.
    """

    audio, sr = librosa.load(
        file_path,
        sr=None
    )

    return audio, sr
