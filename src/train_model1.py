import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score
df = pd.read_csv(
    "data/features.csv"
)
print(df.head())

print()

print(df.info())

print()

print(df.shape)
X = df.drop(
    "Person",
    axis=1
)
y = df["Person"]
X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.2,

    random_state=42

)
print(X_train.shape)

print(X_test.shape)

print(y_train.shape)

print(y_test.shape)
model = RandomForestClassifier(

    random_state=42

)
model.fit(

    X_train,

    y_train

)
predictions = model.predict(

    X_test

)
print(predictions)
accuracy = accuracy_score(

    y_test,

    predictions

)
print(

    "Accuracy:",

    accuracy

)
