import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

data = {
    'text': [
        "I love this product, it is amazing!",
        "This is the worst experience ever.",
        "Absolutely fantastic service and quality.",
        "I hate waiting so long, very disappointing.",
        "The item arrived broken and useless.",
        "Great support team, very helpful.",
        "Not worth the money, do not buy.",
        "Highly recommended, will buy again!",
        "It was okay, nothing special.",
        "Terrible, I want a refund."
    ],
    'label': [
        "Positive", "Negative", "Positive", "Negative",
        "Negative", "Positive", "Negative", "Positive",
        "Neutral", "Negative"
    ]
}

df = pd.DataFrame(data)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = MultinomialNB()
model.fit(X_train, y_train)

acc = accuracy_score(y_test, model.predict(X_test))
print(f"Model Accuracy: {acc}")

while True:
    text = input("\nEnter text to analyze (or 'q' to quit): ")
    if text.lower() == 'q':
        break

    vec_text = vectorizer.transform([text])
    pred = model.predict(vec_text)
    print(f"Result: {pred[0]}")