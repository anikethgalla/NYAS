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

# File uploader
st.subheader("Upload the Student Essay or Assignment:")
uploaded_file = st.file_uploader("Choose a file...", type=["txt", "docx"])

# Submit button
if st.button("Submit"):
    if uploaded_file:
        # Read the uploaded file
        essay_text = uploaded_file.read()

        # Analyze the essay
        num_words, num_sentences, grammar_errors, sentiment, avg_word_length = analyze_essay(essay_text.decode('utf-8'))

        # Check for plagiarism (placeholder)
        example_text = "This is a sample essay for plagiarism detection."
        plagiarism_result = check_plagiarism(essay_text.decode('utf-8'), example_text, n=3, threshold=0.5)

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
st.write("1. Upload the student's essay or assignment using the file uploader above.")
st.write("2. Click the 'Submit' button to get feedback on the essay's word count, sentence count, grammar errors, sentiment, average word length, plagiarism, and grade.")
st.write("3. Review the feedback provided to improve the essay.")
