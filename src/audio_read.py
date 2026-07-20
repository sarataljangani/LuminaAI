import soundfile as sf

# خواندن فایل صوتی
audio, sample_rate = sf.read("data/voice.wav")

print("Sample Rate:", sample_rate)
print("Number of Samples:", len(audio))
print("First 10 Samples:")
print(audio[:10])