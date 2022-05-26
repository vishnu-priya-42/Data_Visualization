from pathlib import Path
from PIL import Image
import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="Data Analysis",page_icon=":chart_with_upwards_trend:",layout="wide")

#Function for displaying graphical content(eg: image)
def Graphical_Content(url) :
    r = requests.get(url)
    if r.status_code != 200 :
        return None
    return r.json()

lottie_coding1 = Graphical_Content("https://assets6.lottiefiles.com/packages/lf20_0yfsb3a1.json")
lottie_coding2 = Graphical_Content("https://iconscout.com/lottie/programming-language-4517710.json")

#displaying website main motive
with st.container():
    left_column, right_column=st.columns((1,2))
    with left_column:
        st_lottie(lottie_coding1,height=300,key="coding")
    with right_column :
        st.title("Data Analysis Report")
        st.subheader("Data Analysis on Automotive Industry")
        st.write("")
        st.markdown("""
        <style>.font {font-size:20px !important;}</style>""", unsafe_allow_html=True)
        st.markdown('<p class="font">This Website summarises the challenge of data analysis on a sample dataset of Automotive Industry</p>', unsafe_allow_html=True)

#displaying summary of website
with st.container():
    st.write("---")
    left_column, right_column=st.columns((1,2))
    with left_column:
        st.header("About Project")
        """
        - The data analysis was done on a dataset cars_engage_2022.csv
    
        - Using the dataset, data was analysed to find out most popular car specification,
            most popular car type and the power of car based on fuel capapcity
      
        - Models were developed to predict the future sales
        """
        st.write("1. Simple Linear Regression Model")
        st.write("2. Multiple Linear Regression Model")
    
        """- Click on below link to view visualized data"""
        st.write("[Data Visualization](https://share.streamlit.io/vishnu-priya-42/abcd/main/website/Data_Visualization.py)")
    with right_column :
        st_lottie(lottie_coding2,height=300)

# ---- Contact form Info
with st.container() :
    st.write("---")
    st.header("My details")
    st.markdown('<p class="font">Name: Vishnu Priya</p>', unsafe_allow_html=True)
    st.markdown('<p class="font">Branch: Computer Science and Engineering</p>', unsafe_allow_html=True)
    st.markdown('<p class="font">College: Maturi Venkata Subba Rao Enginneering College</p>', unsafe_allow_html=True)
    st.markdown('<p class="font">Gihub profile: </p>', unsafe_allow_html=True)
    st.write("[Click Here](https://github.com/vishnu-priya-42/abcd)")
