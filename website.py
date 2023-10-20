import streamlit as st

# Define the external link
url_resources = "https://congnixresources.streamlit.app/"
url_notes = "https://congnixnotes.streamlit.app/"
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


# Add more content as needed
st.write("""Hello student I am Cognix your ai mentor.How may I help you today.\n
         1.For student resources click on student resoruces\n
         2.For notes Click on Notes\n
         3.For submission of assignment and assignment grading click on assignment\n
         4.For online classroom click on online classroom """)