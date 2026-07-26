import librosa
import numpy as np

# خواندن فایل صوتی 
audio, sr = librosa.load("data/voice.wav", sr=None)

#محاسبه zero crossing rate
zcr = librosa.feature.zero_crossing_rate(audio)

#محاسبه میانگین
zcr_mean = np.mean(zcr)

#نمایش خروجی

print(zcr.shape)

print("zero crossing Rate:",zcr.shape)

print("Average ZCR:",zcr_mean)

print(np.mean(zcr))
