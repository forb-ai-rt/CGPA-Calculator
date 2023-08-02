import streamlit as st
import numpy as np

st.set_page_config(
    page_title="CGPA Calculator",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        "Get Help": "https://github.com/Siddhesh-Agarwal/CGPA-Calculator/discussions",
        "Report a bug": "https://github.com/Siddhesh-Agarwal/CGPA-Calculator/issues/new",
        "About": None,
    },
)


grade_to_point = {
    "O": 10,
    "A+": 9,
    "A": 8,
    "B+": 7,
    "B": 6,
    "C": 5,
}
grades = list(grade_to_point.keys())

def calculate_cgpa():
  return pass
