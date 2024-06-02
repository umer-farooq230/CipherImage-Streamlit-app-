import streamlit as st
from streamlit_lottie import st_lottie
import requests
import emoji
st.set_page_config(page_title="Pass Vault", layout="wide")

# Lottie animation URL
lottie_coding = "https://lottie.host/37a5fe59-9803-459f-9b5d-7b7ca37e28ee/JhPOV61Nt3.json"
# Load Lottie animation
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}<style>",unsafe_allow_html=True)
    
local_css("style.css")
# Display Lottie animation
with st.container():
    l_column, r_column = st.columns(2)
    with l_column:
        st.title(":violet[ImagePass]", anchor="title",)
        st.subheader("This tool allows you to hide your password in any image ")
        #st.write("")
        st.write("\n\n")
        st.write(f"This tool is still in progress and will launch very soon. Help us shape this product at the end of this page {emoji.emojize(':smile:')} {emoji.emojize(':down_arrow:')}")


    with r_column:
        st_lottie(lottie_coding, height=280, key="coding")

# Instructions and images
with st.container():
    st.write("---")
    st.header("How does it work?")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("file1.png", caption=" ", use_column_width=True)
        st.subheader("Enter the password you want to save")
    with col2:
        st.image("file2.png", caption=" ", use_column_width=True)
        st.subheader("Select the image you want to encrypt into and press encrypt")
    with col3:
        st.image("file3.png", caption=" ",  use_column_width=True)
        st.subheader("For decryption, select the encrypted image and press decrypt")

with st.container():
    st.write("---")  
    st.header("What are your thoughts about this tool?")
    contact_form="""
    <form action="https://formsubmit.co/ultraflare8@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Your message" required></textarea>
     <button type="submit">Send</button>
    </form>        
    """
    left_column,right_column=st.columns(2)
    with left_column:
        st.markdown(contact_form,unsafe_allow_html=True)
    with right_column:
        st.empty()
