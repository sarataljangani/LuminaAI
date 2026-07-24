import librosa
import matplotlib.pyplot as plt

#خواندن فایل صوتی
audio, sr = librosa.load(
    "data/voice.wav",
    sr=None
)


#رسم شکل موج
plt.figure(figsize=(10,4))

plt.plot(audio)

plt.title("Voice Waveform")

plt.xlabel("Samples")

plt.ylabel("Amplitude")

plt.show()