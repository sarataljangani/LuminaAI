import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ==========================
# خواندن دیتاست
# ==========================

df = pd.read_csv("data/dataset_features.csv")

print("Dataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

# ==========================
# جدا کردن ویژگی ها و برچسب
# ==========================

X = df.drop("speaker_id", axis=1)

y = df["speaker_id"]

# ==========================
# تقسیم داده
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTrain Size:", X_train.shape)
print("Test Size:", X_test.shape)

# ==========================
# ساخت مدل
# ==========================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# ==========================
# آموزش مدل
# ==========================

model.fit(X_train, y_train)

print("\nModel Trained Successfully.")

# ==========================
# پیش بینی
# ==========================

predictions = model.predict(X_test)

# ==========================
# محاسبه دقت
# ==========================

accuracy = accuracy_score(y_test, predictions)

print("\nAccuracy:")
print(accuracy)

# ==========================
# گزارش
# ==========================

print("\nClassification Report:")
print(classification_report(y_test, predictions))

# ==========================
# ماتریس خطا
# ==========================

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))