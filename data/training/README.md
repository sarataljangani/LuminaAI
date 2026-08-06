

# LuminaAI 🎙️ ## AI-powered Speaker Verification System LuminaAI is an Artificial Intelligence based speaker verification system that identifies and verifies speakers using audio signal processing and machine learning techniques. The project extracts important audio features from voice recordings and uses machine learning models to classify and verify speakers. --- ## 🚀 Project Overview Speaker verification is a biometric technology that determines whether a voice belongs to a specific person. LuminaAI pipeline: Audio Input ↓ Audio Preprocessing ↓ Feature Extraction ↓ Machine Learning Model ↓ Speaker Prediction --- ## ✨ Features - Audio signal processing - Feature extraction from speech - Machine learning based speaker classification - Dataset preparation pipeline - Model training and evaluation --- ## 🧠 Technologies Used - Python 3.13 - NumPy - Pandas - Librosa - SoundFile - Scikit-learn - Matplotlib --- ## 📂 Project Structure 

LuminaAI/ │ ├── data/ │ └── training/ │ └── labels.csv │ ├── src/ │ ├── features/ │ │ └── feature_extractor.py │ ├── create_dataset.py │ └── train_model.py │ ├── reports/ │ ├── models/ │ ├── requirements.txt └── README.md

--- ## 🎵 Dataset Audio files are not stored inside this repository because of their large size. Dataset contains: - Speaker audio samples - Audio labels - Extracted feature information To use the project, download the dataset separately and place audio files inside: 

data/training/

--- ## 🔍 Extracted Audio Features The system uses several audio features: - MFCC (Mel Frequency Cepstral Coefficients) - Zero Crossing Rate (ZCR) - Spectral Centroid - Spectral Bandwidth - Spectrogram features These features represent important characteristics of human speech. --- ## ⚙️ Installation Clone the repository:
bash git clone https://github.com/USERNAME/LuminaAI.git 

Install dependencies:

pip install -r requirements.txt 

▶️ Usage

Extract Features

python src/features/feature_extractor.py 

Create Dataset

python src/create_dataset.py 

Train Model

python src/train_model.py 

📊 Machine Learning Pipeline

features.csv | ↓ Data Preprocessing | ↓ Train/Test Split | ↓ Machine Learning Model | ↓ Prediction | ↓ Accuracy Evaluation 

👥 Team

Taljangani

Heidari

Nematzade

Goudarzian

📌 Future Improvements

Deep Learning based speaker verification

Neural network models

Real-time voice recognition

Larger multilingual datasets

📄 License

This project is developed for educational and research purposes.
