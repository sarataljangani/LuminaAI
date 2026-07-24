import librosa
import numpy as np

audio, sr = librosa.load(
    "data/voice.wav",
    sr=None
)
mfcc = librosa.feature.mfcc(
    y=audio,
    sr=sr,
    n_mfcc=13
)
mfcc_mean = np.mean(
    mfcc,
    axis=1
)
print(mfcc.shape)
print(mfcc_mean.shape)

zcr = librosa.feature.zero_crossing_rate(audio)

zcr_mean = np.mean(zcr)
print(zcr_mean)

centroid = librosa.feature.spectral_centroid(
    y=audio,
    sr=sr
)

centroid_mean = np.mean(centroid)
bandwidth = librosa.feature.spectral_bandwidth(
    y=audio,
    sr=sr
)

bandwidth_mean = np.mean(bandwidth)
feature_vector = np.concatenate(

    [

        mfcc_mean,

        [zcr_mean],

        [centroid_mean],

        [bandwidth_mean]

    ]

)
print("Feature Vector:")

print(feature_vector)

print()

print(feature_vector.shape)
def extract_features(file_path):

    audio, sr = librosa.load(
        file_path,
        sr=None
    )

    mfcc = librosa.feature.mfcc(
        y=audio,
        sr=sr,
        n_mfcc=13
    )

    mfcc_mean = np.mean(
        mfcc,
        axis=1
    )

    zcr = np.mean(
        librosa.feature.zero_crossing_rate(audio)
    )

    centroid = np.mean(
        librosa.feature.spectral_centroid(
            y=audio,
            sr=sr
        )
    )

    bandwidth = np.mean(
        librosa.feature.spectral_bandwidth(
            y=audio,
            sr=sr
        )
    )

    features = np.concatenate(

        [

            mfcc_mean,

            [zcr],

            [centroid],

            [bandwidth]

        ]

    )

    return features
features = extract_features(
    "data/voice.wav"
)

print(features)

print(features.shape)

