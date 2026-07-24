import librosa
import numpy as np


 #خواندن فایل صوتی
audio, sr = librosa.load("data/voice.wav", sr=None)


#محاسبه spectral centroid
centroid = librosa.feature.spectral_centroid(
    y=audio,
    sr=sr
)

print("Spectral Cntroid Shape:" , centroid.shape)

print()

print("Average:")

print(np.mean(centroid))
