import librosa
import numpy as np

audio, sr = librosa.load("data/voice.wav", sr=None)

centroid = librosa.feature.spectral_centroid(
    y=audio,
    sr=sr
)

print(centroid)

print()

print("Average:")

print(np.mean(centroid))