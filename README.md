# 🧠 AI Sentiment Analysis Bot

> **Global Hack Week: AI/ML Edition Submission** 🚀

Hi there! 👋 Welcome to my project for **GHW AI/ML Week**. I built this machine learning tool to explore how computers can understand human emotions in text.

## 🧐 What is this?
This is a Command Line Interface (CLI) application that uses **Natural Language Processing (NLP)** to detect the sentiment of a sentence.

You type a review (like *"I loved this workshop!"*), and the AI predicts if it is:
* ✅ **Positive**
* ❌ **Negative**
* 😐 **Neutral**

I built this to get hands-on experience with **Scikit-Learn** and the **Naive Bayes** algorithm.

---

## 🛠️ Tech Stack
* **Language:** Python 3.x 🐍
* **Libraries:** `pandas`, `scikit-learn`
* **Model:** Multinomial Naive Bayes
* **Technique:** Bag-of-Words (CountVectorizer)

---

## 💻 How to Run It
Want to test it out? Follow these steps:

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/captain-vs/sentiment-analysis.git](https://github.com/captain-vs/sentiment-analysis.git)
    cd sentiment-analysis
    ```

2.  **Install dependencies**
    You'll need pandas and scikit-learn installed.
    ```bash
    pip install pandas scikit-learn
    ```

3.  **Run the bot**
    ```bash
    python Main.py
    ```

4.  **Start typing!**
    The bot will train itself instantly and then ask for your input.

---

## 🧠 How It Works (The Logic)
I didn't just want to copy code; I wanted to understand the math! Here is the breakdown of my logic:

1.  **Data Generation:** The script creates a labeled dataset of reviews (e.g., "Great product" = Positive).
2.  **Vectorization:** Computers can't read words, so I used `CountVectorizer` to turn text into numerical vectors (counts of words).
3.  **Splitting:** I split the data into Training (80%) and Testing (20%) sets to validate accuracy.
4.  **Training:** The **Multinomial Naive Bayes** classifier learns the probability of a word belonging to a "Positive" or "Negative" class.
5.  **Prediction:** When you type a sentence, the model calculates the most likely sentiment based on the words it learned.

---

## 🧠 What I Learned
During this challenge, I learned about the importance of **tokenization**—how breaking sentences down into word counts allows a mathematical model to understand context. I also learned how to split data into training and testing sets to ensure the model isn't just memorizing the answers.

---

**Happy Hacking!** ✨
*Built by [Vishnu](https://github.com/captain-vs) for MLH Global Hack Week.*

### **Final Checklist to Submit**
