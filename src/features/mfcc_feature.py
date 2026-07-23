import librosa
import numpy as np

audio, sr = librosa.load("data/voice.wav", sr=None)

mfcc = librosa.feature.mfcc(
    y=audio,
    sr=sr,
    n_mfcc=13
)

print("MFCC Shape:")
print(mfcc.shape)

print("\nMFCC Values:")
print(mfcc)


print()

print(type(mfcc))

print(mfcc.ndim)

print(mfcc.shape)

feature_vector = np.mean(
    mfcc,
    axis=1
)

print(feature_vector)

print(feature_vector.shape)
