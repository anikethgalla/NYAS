# Import necessary libraries and models
import streamlit as st
import spacy
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
import language_tool_python
from gensim.models import Word2Vec

nltk.download('vader_lexicon')
nltk.download('punkt')

# Load NLP models
nlp = spacy.load("en_core_web_sm")
tool = language_tool_python.LanguageTool('en-US')
sia = SentimentIntensityAnalyzer()

# Streamlit UI
st.title("Automated Essay Analysis and Feedback")

# Input text area
st.subheader("Enter the Student Essay or Assignment:")
input_text = st.text_area("Paste the text here:")

# Function to analyze and provide feedback
def analyze_essay(essay):
    # Tokenize the essay using spaCy
    doc = nlp(essay)

    # Calculate the number of words and sentences
    num_words = len(doc)
    num_sentences = len(list(doc.sents))

    # Check grammar using LanguageTool
    grammar_errors = len(tool.check(essay))

    # Calculate sentiment using NLTK's VADER
    sentiment = sia.polarity_scores(essay)

    # Calculate the average word length
    avg_word_length = sum(len(token.text) for token in doc) / num_words if num_words > 0 else 0

    return num_words, num_sentences, grammar_errors, sentiment, avg_word_length

# Function to calculate the grade
def calculate_grade(num_words, grammar_errors, sentiment_score):
    if num_words < 200:
        return "F"
    elif num_words < 500 and grammar_errors < 5 and sentiment_score >= 0.2:
        return "A"
    elif num_words >= 500 and grammar_errors <= 2 and sentiment_score >= 0.4:
        return "A+"
    else:
        return "B"

# Function to check for plagiarism using n-grams
def check_plagiarism(text1, text2, n=3, threshold=0.7):
    ngrams_text1 = calculate_ngrams(text1, n)
    ngrams_text2 = calculate_ngrams(text2, n)

    # Calculate Jaccard similarity between n-grams
    intersection = len(set(ngrams_text1).intersection(ngrams_text2))
    union = len(set(ngrams_text1).union(ngrams_text2))

    jaccard_similarity = intersection / union

    if jaccard_similarity >= threshold:
        return f"Plagiarism detected! Similarity: {jaccard_similarity:.2f}"
    else:
        return "No plagiarism detected."

# Placeholder for plagiarism checking function
def calculate_ngrams(text, n):
    words = nltk.word_tokenize(text.lower())
    n_grams = list(nltk.ngrams(words, n))
    return n_grams

if input_text:
    # Analyze the essay
    num_words, num_sentences, grammar_errors, sentiment, avg_word_length = analyze_essay(input_text)

    # Check for plagiarism (placeholder)
    example_text = "This is a sample essay for plagiarism detection."
    plagiarism_result = check_plagiarism(input_text, example_text, n=3, threshold=0.5)

    # Calculate the grade
    grade = calculate_grade(num_words, grammar_errors, sentiment['compound'])

    st.subheader("Analysis Results:")
    st.write(f"Number of Words: {num_words}")
    st.write(f"Number of Sentences: {num_sentences}")
    st.write(f"Grammar Errors: {grammar_errors}")
    st.write(f"Sentiment Analysis: {sentiment['compound']:.2f} (Negative: {sentiment['neg']:.2f}, Neutral: {sentiment['neu']:.2f}, Positive: {sentiment['pos']:.2f})")
    st.write(f"Average Word Length: {avg_word_length:.2f}")

    st.subheader("Feedback:")
    if grammar_errors > 0:
        st.warning("Grammar issues detected. Consider proofreading your essay.")
    if sentiment['compound'] < -0.2:
        st.warning("Your assignment needs to be worked on.")
    elif sentiment['compound'] > 0.2:
        st.success("The assignment is pretty great.")
    else:
        st.info("The sentiment of your essay is neutral.")

    st.subheader("Plagiarism Check:")
    st.write(plagiarism_result)

    st.subheader("Grade:")
    st.write(f"Grade: {grade}")

# Instructions
st.markdown("### Instructions:")
st.write("1. Paste the student's essay or assignment in the text area above.")
st.write("2. Click enter to get feedback on the essay's word count, sentence count, grammar errors, sentiment, average word length, plagiarism, and grade.")
st.write("3. Review the feedback provided to improve the essay.")
