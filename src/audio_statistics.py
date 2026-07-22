import librosa
import numpy as np

audio, sr = librosa.load(
    "data/voice.wav",
    sr=None
)

print("Mean:", np.mean(audio))

print("Max:", np.max(audio))

print("Min:", np.min(audio))

print("Standard Deviation:", np.std(audio))