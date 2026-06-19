import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# -----------------------------
# Load Dataset
# -----------------------------
data = pd.read_csv("emails.csv")

print("Dataset Loaded Successfully!\n")
print(data.head())

# -----------------------------
# Features and Labels
# -----------------------------
X = data["text"]
y = data["label"]

# -----------------------------
# Convert Text to TF-IDF Features
# -----------------------------
vectorizer = TfidfVectorizer(stop_words="english")

X = vectorizer.fit_transform(X)

# -----------------------------
# Split Dataset
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42
)

# -----------------------------
# Train Model
# -----------------------------
model = MultinomialNB()

model.fit(X_train, y_train)

# -----------------------------
# Predictions
# -----------------------------
predictions = model.predict(X_test)

# -----------------------------
# Accuracy
# -----------------------------
accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

# -----------------------------
# Confusion Matrix
# -----------------------------
print("\nConfusion Matrix")
print(confusion_matrix(y_test, predictions))

# -----------------------------
# Classification Report
# -----------------------------
print("\nClassification Report")
print(classification_report(y_test, predictions))

# -----------------------------
# Test New Email
# -----------------------------
print("\n==============================")
print(" Email Phishing Detector")
print("==============================")

while True:

    email = input("\nEnter Email Text (or type 'exit'): ")

    if email.lower() == "exit":
        print("Program Closed.")
        break

    email_vector = vectorizer.transform([email])

    prediction = model.predict(email_vector)

    if prediction[0] == 1:
        print("\nPrediction: 🚨 PHISHING EMAIL")
    else:
        print("\nPrediction: ✅ SAFE EMAIL")
