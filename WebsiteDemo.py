# Required Modules
#   -----------
from pathlib import Path
from PIL import Image
import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="Data Analysis",page_icon=":chart_with_upwards_trend:",layout="wide")

#Function for displaying graphical content
def Graphical_Content(url) :
    r = requests.get(url)
    if r.status_code != 200 :
        return None
    return r.json()

lottie_coding1 = Graphical_Content("https://assets6.lottiefiles.com/packages/lf20_0yfsb3a1.json")

with st.container():
    left_column, right_column=st.columns((1,2))
    with left_column :
        st.title("Data Analysis Report")
        st.subheader("Data Analysis on Automotive Industry")
        st.write("")
        st.write("This Website summarises the challenge of data analysis on a sample dataset of Automotive Industry")
    with right_column:
        st_lottie(lottie_coding1,height=300,key="coding")


# ---- graphical images
with st.container():
    st.write("---")
    st.header("About Project")
    """

    - The data analysis was done on a dataset cars_engage_2022.csv
    
    - Using the dataset, data was analysed to find out most popular car specification,
      most popular car type and the power of car based on fuel capapcity
      
    - Models were developed to predict the future sales
         1. Simple Linear Regression Model
         2. Multiple Linear Regression Model
    
    - Click on below link to view visualized data
    
    """

st.write("[Data Visualization](http://localhost:8502/)")

# ---- Contact form Info
with st.container() :
    st.write("---")
    st.header("My details")
    st.write("Name: Vishnu Priya")
    st.write("Branch: Computer Science and Engineering")
    st.write("College: Maturi Venkata Subba Rao Enginneering College")
    
