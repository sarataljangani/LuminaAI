import librosa
import librosa.display
import matplotlib.pyplot as plt

audio, sr = librosa.load("data/voice.wav", sr=None)

stft = librosa.stft(audio)

spectrogram = librosa.amplitude_to_db(abs(stft))

plt.figure(figsize=(10,5))

librosa.display.specshow(
    spectrogram,
    sr=sr,
    x_axis="time",
    y_axis="hz"
)

plt.colorbar()

plt.title("Spectrogram")

plt.show()