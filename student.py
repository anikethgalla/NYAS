import streamlit as st
import pandas as pd
import numpy as np
import subprocess

# Set the title of the dashboard
st.title("Stduent Dashboard")

# Create a sidebar for user input

if st.sidebar.button("Resources",):
            try:
                python_executable = "python"
                
                # Replace "NLP.py" with the correct path to your script
                script_path = r"C:\Users\archa\.vscode\NYAS\Notetaking.py"
                
                # Run the Python script using subprocess
                result = subprocess.run([python_executable, script_path], capture_output=True, text=True)
                st.text(result.stdout)
            except subprocess.CalledProcessError as e:
                st.error(f"Error running the script: {e}")
            except FileNotFoundError:
                st.error("Python script 'my_script.py' not found.")

