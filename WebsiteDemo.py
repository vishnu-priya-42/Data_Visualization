from pathlib import Path
from PIL import Image
import streamlit as st
from streamlit_lottie import st_lottie
import requests
#Eemoji Here : https://www.webfx.com/tools/emoji-cheat-cheet/.
st.set_page_config(page_title="My Webpage",page_icon=":tada:",layout="wide")

def load_lottieurl(url) :
    r = requests.get(url)
    if r.status_code != 200 :
        return None
    return r.json()

def local_css(file_name) :
    with open(file_name) as f :
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
local_css("FontStyle.css")



lottie_coding1 = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_v4isjbj5.json")
#lottie_coding2 = load_lottieurl("https://lottiefiles.com/71619-coding")
#img1 = Image.open("Images/Graphs.png")
#img2 = Image.open("Image/screenshot(33).png")


# ---- Subheading 
with st.container():
    st.subheader("Heyyyy man, This is   Vishnu Priya :wave:")
    st.title("A Data analyst from MVSR Engineering College")
    #file = open("DataAnalysiss.txt","r")
    #print(st.write(file.read()))
st.write("[Learn More >](http://localhost:8501)")



# ---- graphical images
with st.container():
    st.write("---")
    left_column,right_column = st.columns(2)
    with left_column :
        st.header("What I do")
        st.write("##")
    with right_column:
        st_lottie(lottie_coding1,height=300,key="coding")
        #st.lottie(lottie_coding2,height=300,key="coding")


# ---- Image and description sort of thing
with st.container() :
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        #Inserting an image (Bug is done)
        st.write("We can insert our images here")
        #st.image(img1)
        #st.image(img2)
    with text_column:
        st.subheader("Intergrate lottie Animations inside")
        st.write("\n\n\nWe can write our content here....")
        st.markdown("[Provide any link...](_Provide any link here....)")



# ---- Contact form Info
with st.container() :
    st.header("Get in touch with me")
    st.write("##")
    contact_form = """
    <form action="https://formsubmit.co/vishnupriya21202@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Name " required>
        <input type="email" name="Your Name" placeholder="your@gmail.com" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>"""
    left_column,right_column=st.columns(2)
    with left_column:
        st.markdown(contact_form,unsafe_allow_html=True)
    with right_column :
        st.empty()
