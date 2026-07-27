import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score

from sklearn.ensemble import RandomForestClassifier

from sklearn.neighbors import KNeighborsClassifier

from sklearn.tree import DecisionTreeClassifier

from sklearn.svm import SVC
df = pd.read_csv("data/features.csv")
print(df.head())

print(df.shape)

print(df.info())
X = df.drop("speaker_id", axis=1)
y = df["speaker_id"]
X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.2,

    random_state=42,

    stratify=y

)
models = {

    "Random Forest":

        RandomForestClassifier(random_state=42),

    "KNN":

        KNeighborsClassifier(n_neighbors=5),

    "Decision Tree":

        DecisionTreeClassifier(random_state=42),

    "SVM":

        SVC()

}
results = []
for name, model in models.items():

    model.fit(

        X_train,

        y_train

    )

    prediction = model.predict(

        X_test

    )

    accuracy = accuracy_score(

        y_test,

        prediction

    )

    results.append(

        [name, accuracy]

    )

    print(name)

    print(accuracy)

    print("----------------")
    result_df = pd.DataFrame(

    results,

    columns=[

        "Model",

        "Accuracy"

    ]

)

print(result_df)
best = result_df.loc[

    result_df["Accuracy"].idxmax()

]

print()

print("Best Model")

print(best)
