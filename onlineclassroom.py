import streamlit as st
import pandas as pd

# Create a DataFrame with class information
data = {
    'Class Name': ['Math 101', 'Physics 202', 'History 101'],
    'Instructor': ['John Doe', 'Jane Smith', 'Robert Johnson'],
    'Class Link': [
        'https://example.com/math101',
        'https://example.com/physics202',
        'https://example.com/history101'
    ]
}

df = pd.DataFrame(data)

# Set the page title
st.title("Online Classroom Links")
st.write("""
For successful online classes, prepare in advance, access class links, engage actively, test equipment, ask questions, and minimize distractions. Take notes, participate in discussions, and stay motivated. 
Connect with peers, provide feedback for improvement, and stay organized to make the most of your virtual learning experience.""")

# Display the DataFrame in a Streamlit table
st.dataframe(df, width=600, height=300)


