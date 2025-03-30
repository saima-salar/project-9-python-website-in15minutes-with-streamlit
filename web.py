#Project 9: Build a Python Website in 15 Minutes With Streamlit
# Project 9: Build a Python Website in 15 Minutes With Streamlit

import streamlit as st
import pandas as pd
import random

# Set Streamlit page configuration
st.set_page_config(page_title="Student Data Generator", layout="wide")

# Title of the app
st.title("Student CSV File Generator")

# Student data list
names = ["John", "Jane", "Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah"]
students = []

# Generate student records
for i in range(1, 11):  # Generate 10 students (1-10)
    student = {
        "ID": i,
        "Name": random.choice(names),
        "Age": random.randint(18, 25),
        "Grade": random.choice(["A", "B", "C", "D", "F"]),
        "Marks": random.randint(40, 100)
    }
    students.append(student)

# Convert student records into a DataFrame
df = pd.DataFrame(students)

# Display the generated student data
st.subheader("Generated Students Data")
st.dataframe(df)

# Convert dataframe to CSV format
csv_file = df.to_csv(index=False).encode('utf-8')

# Add a unique key to download button to avoid duplicate element ID error
st.download_button("Download CSV File", csv_file, "students.csv", "text/csv", key="download_csv")

# Show success message
st.success("Students Record Generated Successfully!")
