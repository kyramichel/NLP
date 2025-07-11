# sentiment_demo.py

# 1. Rule-based with TextBlob
from textblob import TextBlob

def sentiment_textblob(text: str):
    blob = TextBlob(text)
    # Polarity: –1 (negative) to +1 (positive)
    # Subjectivity: 0 (objective) to 1 (subjective)
    return {
        "polarity": blob.sentiment.polarity,
        "subjectivity": blob.sentiment.subjectivity
    }


# 2. Machine-learning with scikit-learn (Naive Bayes)
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split

# For demonstration purposes we use a tiny toy dataset.
TRAIN_TEXTS = [
    "I love this product, it’s amazing!",
    "That was the worst experience ever.",
    "Absolutely fantastic service.",
    "I hate this. So bad.",
    "Very happy with the results!",
    "Terrible, I will never buy again."
]
TRAIN_LABELS = ["positive", "negative", "positive", "negative", "positive", "negative"]

# Train a simple pipeline once
ml_pipeline = make_pipeline(CountVectorizer(), MultinomialNB())
ml_pipeline.fit(TRAIN_TEXTS, TRAIN_LABELS)

def sentiment_naive_bayes(text: str):
    pred = ml_pipeline.predict([text])[0]
    # We can also get a probability if we like:
    probas = ml_pipeline.predict_proba([text])[0]
    # Map label→prob
    label_proba = dict(zip(ml_pipeline.classes_, probas))
    return {
        "label": pred,
        "probabilities": label_proba
    }


# 3. Transformer-based with Hugging Face
from transformers import pipeline

# This will download a small fine-tuned sentiment model
hf_pipeline = pipeline("sentiment-analysis")

def sentiment_transformer(text: str):
    result = hf_pipeline(text)[0]
    # e.g. { 'label': 'POSITIVE', 'score': 0.9998 }
    return result


# Main driver
if __name__ == "__main__":
    TEXT = "I’m absolutely thrilled with how this demo turned out!"

    print("Input Text:", TEXT, "\n")

    # 1. TextBlob
    tb_result = sentiment_textblob(TEXT)
    print("1) TextBlob (rule-based)")
    print(f"   polarity: {tb_result['polarity']:.3f}")
    print(f"   subjectivity: {tb_result['subjectivity']:.3f}\n")

    # 2. Naive Bayes
    nb_result = sentiment_naive_bayes(TEXT)
    print("2) Naive Bayes (scikit-learn)")
    print(f"   predicted label: {nb_result['label']}")
    print(f"   probabilities: {nb_result['probabilities']}\n")

    # 3. Transformer
    tf_result = sentiment_transformer(TEXT)
    print("3) Transformer (Hugging Face)")
    print(f"   label: {tf_result['label']}")
    print(f"   score: {tf_result['score']:.3f}")
