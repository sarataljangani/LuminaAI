import soundfile as sf

audio, sample_rate = sf.read("data/voice.wav")

print("Sample Rate:", sample_rate)

print("Number of Samples:", len(audio))

print("Duration:", len(audio)/sample_rate)
