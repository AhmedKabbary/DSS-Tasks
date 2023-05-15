import pandas as pd
from joblib import dump
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

features = pd.read_csv('gender_classification_v7.csv')

X_train, X_test, Y_train, Y_test = train_test_split(
    features.drop('gender', axis=1), features['gender'], test_size=0.2)

model = LogisticRegression()
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

accuracy = accuracy_score(Y_test, Y_pred)
print(accuracy*100)

dump(model, 'model.joblib')
