import streamlit as st
from datetime import datetime

# Title for the web app
st.title(" Note Taking")

# Text input for note-taking
note = st.text_area("Take notes:")

# Button to save the note
if st.button("Save Note"):
    if note:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('notes.txt', 'a') as note_file:
            note_file.write(f"{now}: {note}\n")
        st.success("Note saved successfully!")

# Display existing notes
st.header("Existing Notes:")
with open('notes.txt', 'r') as note_file:
    for line in note_file:
        st.write(line)

st.text("Note: This is a simple text-based note-taking application. ")