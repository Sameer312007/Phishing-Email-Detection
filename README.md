# Phishing Email Detection Model

## Overview

This project uses Machine Learning (Scikit-learn) to classify emails as either **Phishing** or **Safe** using Natural Language Processing (NLP).

---

## Features

- Detect phishing emails
- TF-IDF feature extraction
- Naive Bayes Classification
- Accuracy Calculation
- Confusion Matrix
- Classification Report
- Predict custom email text

---

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Machine Learning

---

## Project Structure

```
Phishing-Email-Detection/
│
├── phishing_detector.py
├── emails.csv
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
python phishing_detector.py
```

---

## Example Output

```
Model Accuracy: 100.0%

Confusion Matrix

[[3 0]
 [0 3]]
```

---

## Example Prediction

Input:

```
Urgent! Verify your bank account immediately.
```

Output:

```
Prediction: PHISHING EMAIL
```

Input:

```
Meeting has been rescheduled to tomorrow.
```

Output:

```
Prediction: SAFE EMAIL
```

---

## Author

Your Name
