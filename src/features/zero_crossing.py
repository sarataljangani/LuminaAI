import librosa
import numpy as np

# خواندن فایل صوتی 
audio, sr = librosa.load("data/voice.wav", sr=None)

#محاسبه zero crossing rate
zcr = librosa.feature.zero_crossing_rate(audio)

print(zcr.shape)

print("zero crossing Rate:")

print("Average ZCR:")

print(np.mean(zcr))
