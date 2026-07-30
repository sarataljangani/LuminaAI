import joblib

model = joblib.load(
    "models/speaker_model.pkl"
)
extract_features()
feature = pd.DataFrame(
    [feature]
)
prediction = model.predict(
    feature
)
print(
    prediction
)