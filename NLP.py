import streamlit as st
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
import language_tool_python
from gensim.models import Word2Vec
from docx import Document
import io
import re

nltk.download('vader_lexicon')
nltk.download('punkt')

# Initialize NLP models
sia = SentimentIntensityAnalyzer()
tool = language_tool_python.LanguageTool('en-US')

# Function to count words
def count_words(text):
    words = nltk.word_tokenize(text)
    return len(words)

# Function to count sentences
def count_sentences(text):
    sentences = nltk.sent_tokenize(text)
    return len(sentences)

# Function to check grammar errors
def check_grammar(text):
    errors = tool.check(text)
    return len(errors)

# Function to analyze sentiment
def analyze_sentiment(text):
    sentiment = sia.polarity_scores(text)
    return sentiment

# Function to calculate average word length
def average_word_length(text):
    words = nltk.word_tokenize(text)
    total_word_length = sum(len(word) for word in words)
    return total_word_length / len(words) if len(words) > 0 else 0

# Function to calculate the grade
def calculate_grade(num_words, grammar_errors, compound_sentiment):
    # You can define your grading logic here based on the provided metrics
    grade = "A"  # Placeholder grade
    return grade

# Streamlit UI
st.title("Automated Essay Analysis and Feedback")

# File uploader
st.subheader("Upload the Student Essay or Assignment:")
uploaded_file = st.file_uploader("Choose a file...", type=["txt", "docx"])

# Submit button
if st.button("Submit"):
    if uploaded_file:
        if uploaded_file.type == "text/plain":
            essay_text = uploaded_file.read().decode('utf-8')
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            doc = Document(io.BytesIO(uploaded_file.read()))
            essay_text = ' '.join([p.text for p in doc.paragraphs])

        num_words = count_words(essay_text)
        num_sentences = count_sentences(essay_text)
        grammar_errors = check_grammar(essay_text)
        sentiment = analyze_sentiment(essay_text)
        avg_word_length = average_word_length(essay_text)

        # Check for plagiarism (placeholder)
        example_text = "This is a sample essay for plagiarism detection."
        plagiarism_result = "No plagiarism detected"  # Placeholder

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
st.write("1. Upload the student's essay or assignment using the file uploader above.")
st.write("2. Click the 'Submit' button to get feedback on the essay's word count, sentence count, grammar errors, sentiment, average word length, plagiarism, and grade.")
st.write("3. Review the feedback provided to improve the essay.")
