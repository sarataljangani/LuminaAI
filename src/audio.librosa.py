import librosa

audio, sample_rate = librosa.load(
    "data/voice.wav",
    sr=None
)

print("Sample Rate:", sample_rate)

print("Shape:", audio.shape)

print("Duration:", len(audio)/sample_rate)
