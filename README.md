# SMS Spam Detection

A lightweight machine learning project that classifies SMS messages as **Spam** or **Ham** using **TF-IDF** feature extraction and **Multinomial Naive Bayes**.

The project focuses on understanding and implementing a complete traditional NLP classification pipeline, from text vectorization to model evaluation and deployment.

## How It Works

```text
SMS Message
    ↓
TF-IDF Vectorization
    ↓
Multinomial Naive Bayes
    ↓
Spam / Ham Prediction
```

TF-IDF converts SMS text into numerical features based on the importance of words across the dataset.

Multinomial Naive Bayes then uses these features to determine whether a message is likely to be spam or legitimate.

## Dataset

This project uses the **Super SMS Dataset**, a large SMS spam corpus containing approximately **67,000 labeled messages**.

The dataset contains both:

- Ham / legitimate SMS messages
- Spam SMS messages

Dataset repository:

https://github.com/smspamresearch/spstudy

Associated research:

> Muhammad Salman, Muhammad Ikram, and Mohamed Ali Kaafar,  
> *Investigating Evasive Techniques in SMS Spam Filtering: A Comparative Analysis of Machine Learning Models*,  
> IEEE Access, 2024.

## Model

The classifier uses:

- **TF-IDF Vectorization**
- **Multinomial Naive Bayes**
- Train/Test Split
- Scikit-learn

The trained model is exported using Python's `pickle` module so that it can be loaded later without retraining.

## Results

The model was evaluated on **16,753 unseen SMS messages**.

### Classification Performance

| Metric | Ham | Spam |
|---|---:|---:|
| Precision | 0.98 | 0.98 |
| Recall | 0.99 | 0.97 |
| F1 Score | 0.98 | 0.98 |

**Overall Accuracy: ~98.09%**

### Confusion Matrix

```text
[[10050, 132],
 [  188, 6383]]
```

This means:

- **10,050** legitimate messages were correctly classified as Ham
- **6,383** spam messages were correctly detected
- **132** legitimate messages were incorrectly classified as Spam
- **188** spam messages were incorrectly classified as Ham

## Project Structure

```text
sms-spam-detection/
│
├── dataset/
│
├── model/
│   └── model.pkl
│
├── notebook/
│
├── app.py
├── requirements.txt
└── README.md
```

The exact structure may vary depending on deployment.

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd <repository-name>
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Load the trained model and TF-IDF vectorizer and provide an SMS message as input.

Example:

```text
Congratulations! You have won a free prize. Click here to claim now.
```

Output:

```text
SPAM
```

Example:

```text
Hey, are you coming to class today?
```

Output:

```text
HAM
```

## Technologies Used

- Python
- Pandas
- Scikit-learn
- TF-IDF
- Multinomial Naive Bayes
- Pickle

## Future Improvements

Possible improvements include:

- TF-IDF bigrams
- Character-level n-grams
- Naive Bayes hyperparameter tuning
- Prediction threshold tuning
- Comparing Logistic Regression and Linear SVM
- Deploying the trained model through a simple web interface

## Local Deployment

The SMS spam detection API is currently deployed and running locally using Flask and Connexion.

The API is served on localhost and accepts SMS messages through the `/api/predict` endpoint, returning a prediction for each message:

- `0` → Ham
- `1` → Spam

Example local endpoint:

```text
http://localhost:5000/api/predict
```

The API specification is defined using Swagger/OpenAPI and can be tested locally before moving to a public deployment platform.

## Disclaimer

This project is intended as an educational machine learning project. Real-world spam filtering systems use additional information such as sender reputation, URLs, metadata, and other security signals alongside text classification.

## Acknowledgements

Thanks to the authors of the **Super SMS Dataset** for making the dataset available for SMS spam research.