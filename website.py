import streamlit as st
import pandas as pd

# Define the external link
url_resources = "https://congnixresources.streamlit.app/"
url_notes = "https://congnixnotes.streamlit.app/"
url_physicslab="https://www.physicsclassroom.com/"
url_chemsirtlab="http://chemcollective.org/"
# Create the Streamlit web app
st.set_page_config(
    page_title="Simple Website",
    page_icon=":link:",
    layout="wide"
)

# Add content to the website
st.title("Cognix")

st.sidebar.title('Dashboard')
st.sidebar.link_button("Student resources", url_resources)
st.sidebar.link_button("Notes", url_notes)
st.sidebar.link_button("Physics lab", url_physicslab)
st.sidebar.link_button("Chemistry lab", url_chemsirtlab)

# Add more content as needed
st.write("""Hello student I am Cognix your ai mentor.How may I help you today.\n
         1.For student resources click on student resoruces\n
         2.For notes Click on Notes\n
         3.For submission of assignment and assignment grading click on assignment\n
         4.For online classroom click on online classroom """)

# Create a sample timetable DataFrame
data = {
    'Time': ['9:00 AM', '10:00 AM', '11:00 AM', '12:00 PM', '1:00 PM'],
    'Monday': ['AP Chemistry', 'AP physics', 'Honours English', 'Lunch', 'AP Calulus'],
    'Tuesday': ['AP Calculus', 'AP World History', 'Physical Education', 'Lunch', 'Honours English'],
    'Wednesday': ['Photogrpahy club', 'MUN club', 'Chemistry lab', 'Lunch', 'Physicis lab'],
    'Thrusday': ['AP-Politics', 'Honours Biology', 'Honours Biology', 'Lunch', 'AP chemistry'],
    'Friday': ['AP Chemistry', 'AP physics', 'Honours English', 'Lunch', 'AP Calulus'],
}

df = pd.DataFrame(data)

st.title("Your timetable")
# Display the timetable using st.table
st.table(df)