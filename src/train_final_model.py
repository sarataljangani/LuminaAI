import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("data/features.csv")

X = df.drop("speaker_id", axis=1)

y = df["speaker_id"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(
    random_state=42
)

model.fit(X_train, y_train)
joblib.dump(
    model,
    "models/speaker_model.pkl"
)

prediction = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    prediction
)

print("Accuracy:", accuracy)