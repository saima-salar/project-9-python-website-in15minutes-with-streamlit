# Project 9: Build a Python Website in 15 Minutes With Streamlit

import streamlit as st
import pandas as pd
import random

# Set Streamlit page configuration
st.set_page_config(page_title="Student Data Generator", layout="wide")

# Center-align the title
st.markdown("<h1 style='text-align: center;'>Student CSV File Generator</h1>", unsafe_allow_html=True)

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

# Center-align subheader
st.markdown("<h2 style='text-align: center;'>Generated Students Data</h2>", unsafe_allow_html=True)

# Custom CSS to center table column values
st.markdown(
    """
    <style>
        /* Center-align all column values */
        table td, table th {
            text-align: center !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the DataFrame with centered column values
st.dataframe(df.style.set_properties(**{'text-align': 'center'}))

# Convert dataframe to CSV format
csv_file = df.to_csv(index=False).encode('utf-8')

# Center-align the download button
st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
st.download_button("Download CSV File", csv_file, "students.csv", "text/csv", key="download_csv")
st.markdown("</div>", unsafe_allow_html=True)

# Center-align success message
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.success("Students Record Generated Successfully!")
st.markdown("</div>", unsafe_allow_html=True)
