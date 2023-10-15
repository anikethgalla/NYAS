import streamlit as st
import pandas as pd

# Title and description
st.title("Student Database")
st.write("This is a simple student database application.")

# Load student data
@st.cache  # Caches the data to improve performance
def load_data():
    data = pd.read_excel("C:\Users\archa\.vscode\NYAS\student_data.xlsx", engine="openpyxl")  # You can use any data source
    return data

data = load_data()

# Sidebar
st.sidebar.subheader("Add New Student")
new_name = st.sidebar.text_input("Name")
new_age = st.sidebar.number_input("Age", 0, 150, 0)
new_grade = st.sidebar.number_input("Grade", 0, 100, 0)

if st.sidebar.button("Add"):
    data = data.append({"Name": new_name, "Age": new_age, "Grade": new_grade}, ignore_index=True)
    st.sidebar.text("Student Added")

# Display student data
st.subheader("Student List")
st.write(data)

# Export data to Excel
if st.button("Export Data to Excel"):
    data.to_excel("student_data.xlsx", engine="openpyxl", index=False)
    st.success("Data exported to Excel.")

# Data visualization (optional)
st.subheader("Data Visualization")
st.bar_chart(data["Grade"])

# Data summary (optional)
st.subheader("Data Summary")
st.write(data.describe())

