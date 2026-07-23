import librosa
import numpy as np

audio, sr = librosa.load("data/voice.wav", sr=None)

zcr = librosa.feature.zero_crossing_rate(audio)

print(zcr)

print()

print("Average ZCR:")

print(np.mean(zcr))
