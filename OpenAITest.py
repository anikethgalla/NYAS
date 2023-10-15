import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load credentials from environment variables
load_dotenv()
os.environ['OPENAI_ORG'] = 'org-mGxm1ZfQSxaY8CvQ440SIR0Q'
os.environ['OPENAI_API_KEY'] = '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'

# Create a dictionary of standardized tests
standardized_tests = {
    "SAT": {"Country": "United States", "Max Score": 1600},
    "ACT": {"Country": "United States", "Max Score": 36},
    "GRE": {"Country": "International", "Max Score": None},  # GRE doesn't have a fixed maximum score
    "TOEFL": {"Country": "International", "Max Score": 120},
    "GMAT": {"Country": "International", "Max Score": 800},
    "MCAT": {"Country": "United States and Canada", "Max Score": 528},
    "LSAT": {"Country": "United States", "Max Score": 180},
    "IELTS": {"Country": "International", "Max Score": 9},
    "PISA": {"Country": "International", "Max Score": None},  # PISA is a scale, not a maximum score
    "AP": {"Country": "United States", "Max Score": 5},
    "JEE": {"Country": "India", "Max Score": None},  # JEE is a ranking exam, not a score-based test
    "NEET": {"Country": "India", "Max Score": None},  # NEET is a ranking exam, not a score-based test
    "GCSE": {"Country": "United Kingdom", "Max Score": None},  # GCSE grades are letters, not numerical scores
    "Baccalauréat": {"Country": "France", "Max Score": None},  # Baccalauréat has a grading scale, not a numerical score
}

# Streamlit UI
st.title("Curriculum Suggestion")

# Input form
st.sidebar.header("Input Information")

# Input grade
grade = st.sidebar.slider("Grade", 1, 12, 9)

# Input name
name = st.sidebar.text_input("Name")

# Input academic scores
academic_scores = st.sidebar.number_input("Academic Scores (Previous Year)", min_value=0.0)

# Input SAT score
sat_score = st.sidebar.number_input("SAT Score", min_value=0.0, max_value=1600.0)

# Input standardized tests
standardized_test = st.sidebar.selectbox("Standardized Test", list(standardized_tests.keys()))

# Input country and state
country = st.sidebar.text_input("Country")
state = st.sidebar.text_input("State")

if st.sidebar.button("Submit"):
    # Curriculum suggestion based on inputs
    st.header("Curriculum Suggestion")

# Simple rule-based curriculum suggestion
if grade <= 8:
    curriculum = "Middle School Curriculum"
elif grade == 9 or grade == 10:
    curriculum = "High School Curriculum (Preparation for College)"
else:
    curriculum = "College Prep Curriculum"

# Generate curriculum using OpenAI
def query_openai():
    prompt = f"Generate a curriculum for {name}, a {grade}-grade student from {country} with academic scores of {academic_scores} and an SAT score of {sat_score}. They took the {standardized_tests.get(standardized_test, 'N/A')}."
    
    openai.organization = os.environ['OPENAI_ORG']
    openai.api_key = os.environ['OPENAI_API_KEY']
    # Temperature is a measure of randomness
    # Max_tokens is the number of tokens to generate
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.3,
        max_tokens=80,
    )
    
    return response.choices[0].text

# Display the suggested curriculum
suggested_curriculum = query_openai()
st.write(f"Dear {name}, based on your inputs, we suggest the following curriculum:")
st.write(f"Grade: {grade}")
st.write(f"Academic Scores (Previous Year): {academic_scores}")
st.write(f"SAT Score: {sat_score}")
st.write(f"Standardized Test: {standardized_tests.get(standardized_test, 'N/A')}")
st.write(f"Country: {country}")
st.write(f"State: {state}")
st.write(f"Curriculum Suggestion:")
st.write(suggested_curriculum)
