import streamlit as st
import pandas as pd

# Define the external link
url_resources = "https://congnixresources.streamlit.app/"
url_notes = "https://congnixnotes.streamlit.app/"
url_physicslab="https://www.physicsclassroom.com/"
url_chemsirtlab="http://chemcollective.org/"
url_onlineclassrooms="https://cognixclassrooms.streamlit.app/"
# Create the Streamlit web app
st.set_page_config(
    page_title="Cognix",
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
st.sidebar.link_button("Online Classrooms", url_onlineclassrooms)
st.sidebar.button("Assignment submission")

# Add more content as needed
st.write("""Hello student I am Cognix your ai mentor.How may I help you today.\n
         1.For student resources click on student resoruces\n
         2.For notes Click on Notes\n
         3.For submission of assignment and assignment grading click on assignment\n
         4.For online classroom click on online classroom """)

data = {
    'Month': ['January', 'February', 'March', 'April', 'May'],
    'Marks': [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

# Display the DataFrame as a table
st.write("Your progress")


# Create a line chart
chart = st.line_chart(
    df.set_index('Month')['Marks'],
    use_container_width=True,  # Use the full container width
    width=300,  # Set the chart width
    height=200  # Set the chart height
)

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

st.title("Your Assignments")
data1 = {
    'Assignment Name': ['AP calculus Assingment', 'AP chemistry assignment', 'AP world history Assingment'],
    'Submission Date': ['2023-10-01', '2023-10-05', '2023-10-10']
}
df1 = pd.DataFrame(data1)
st.table(df1)