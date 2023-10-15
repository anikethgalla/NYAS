import streamlit as st
import subprocess

# Define the usernames and passwords for students and administrators
student_credentials = {'student1': 'password1', 'student2': 'password2'}
admin_credentials = {'admin1': 'adminpassword1', 'admin2': 'adminpassword2'}

# Create a function to validate credentials
def validate_credentials(credentials, input_username, input_password):
    if input_username in credentials and credentials[input_username] == input_password:
        return True
    return False

# Define the main application
def main():
    st.title("Login Page")
    
    # Add a select box to choose user type (Student or Administrator)
    user_type = st.selectbox("Select User Type", ["Student", "Administrator"])
    
    # Add text input boxes for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    # Check if the login button is clicked
    if st.button("Login"):
        if user_type == "Student" and validate_credentials(student_credentials, username, password):
            st.success("Logged in as a Student")
            # Launch the student dashboard app
            subprocess.run(["streamlit", "run", "C:\Users\archa\.vscode\NYAS\student.py"])
        elif user_type == "Administrator" and validate_credentials(admin_credentials, username, password):
            st.success("Logged in as an Administrator")
            # Launch the administrator dashboard app
            subprocess.run(["streamlit", "run", "admin_dashboard.py"])
        else:
            st.error("Incorrect username or password")

if __name__ == '__main__':
    main()