import streamlit as st
from streamlit_lottie import st_lottie
import requests
import subprocess
import os

st.set_page_config(page_title="Image Pass", layout="wide")

# Lottie animation URL
lottie_coding ="https://lottie.host/1853f5b4-4998-4cea-b64d-7d9e6a0351b6/Fb1o8zjsu5.json"

# Load Lottie animation
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def local_css(filename):
    with open (filename) as f:
        st.markdown(f"<style>{f.read()}<style>",unsafe_allow_html=True)
local_css("style.css")


# Display Lottie animation
with st.container():
    l_column, r_column = st.columns(2)
    with l_column:
        st.title("ImagePass ", anchor="title")
        st.subheader(":lock: Secure your passwords in plain sight! :lock:")
        st.write("Hide your passwords within images effortlessly. Upload an image, input your password, and let our tool seamlessly embed it into the image. Keep your passwords private with our intuitive and secure steganography solution. Start encoding and decoding hidden passwords now!!")
    with r_column:
        st_lottie(load_lottie(lottie_coding), height=300, key="coding")

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
        st.image("file3.png", caption=" ", use_column_width=True)
        st.subheader("For decryption, select the encrypted image and press decrypt")

# EXE file execution
with st.container():
    st.write("---")
    st.header("Hit the button to run the app")

    # Specify the EXE file path
    exe_file_path = "main.exe"

    if st.button("Lets Hide passwords",key="hide_button",):
        if os.path.exists(exe_file_path):
            try:
                # Use subprocess to run the EXE file
                result = subprocess.run([exe_file_path], capture_output=True, text=True)
                st.write("Execution errors:")
                st.write(result.stderr)
            except subprocess.CalledProcessError as e:
                st.write(f"An error occurred while running the file: {e}")
            except RuntimeError as e:
                st.write(f"Runtime error: {e}")
            except Exception as e:
                st.write(f"An unexpected error occurred: {e}")
        else:
            st.write(f"EXE file not found at {exe_file_path}")

# Contact form
with st.container():
    st.write("---")
    st.header("What are your thoughts about this tool?")
    contact_form = """
    <form action="https://formsubmit.co/umerfarooq230@email.com" method="POST">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Your message" required></textarea>
     <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
