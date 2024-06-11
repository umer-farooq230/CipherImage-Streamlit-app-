import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image
import numpy as np
import io

st.set_page_config(page_title="ImagePass", layout="wide", page_icon="🔒")

lottie_coding = "https://lottie.host/1853f5b4-4998-4cea-b64d-7d9e6a0351b6/Fb1o8zjsu5.json"

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Ensure the correct path to style.css
css_path = os.path.join(os.path.dirname(__file__), "style.css")
local_css(css_path)

def encode_text(text, encoding='utf-8', errors='replace'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def decode_text(bits, encoding='utf-8', errors='replace'):
    byte_array = bytearray()
    for i in range(0, len(bits), 8):
        byte = bits[i:i + 8]
        if len(byte) == 8:
            byte_array.append(int(byte, 2))
    return byte_array.decode(encoding, errors)

def encode_in_image(image, text_message):
    try:
        input_im = Image.open(image).convert("RGB")
        image_array = np.array(input_im)
        flat_array = image_array.flatten()

        encoded_text = encode_text(text_message + "<STOP>")
        encoded_bits = list(map(int, encoded_text))

        if len(encoded_bits) > len(flat_array):
            raise ValueError("Message is too long to be encoded in the image.")

        for i, bit in enumerate(encoded_bits):
            flat_array[i] = (flat_array[i] & ~1) | bit

        encoded_image_array = flat_array.reshape(image_array.shape)
        encoded_image = Image.fromarray(encoded_image_array.astype(np.uint8))
        return encoded_image
    except Exception as e:
        raise ValueError(f"Error encoding message into image: {str(e)}")

def extract_from_image(image):
    try:
        encoded_im = np.array(Image.open(image).convert("RGB"))
        flat_array = encoded_im.flatten()

        extracted_bits = ""
        stop_marker = "<STOP>"
        stop_marker_bits = encode_text(stop_marker)

        for pixel in flat_array:
            extracted_bits += str(pixel & 1)
            if extracted_bits.endswith(stop_marker_bits):
                extracted_bits = extracted_bits[:-len(stop_marker_bits)]
                break

        decoded_message = decode_text(extracted_bits)
        return decoded_message
    except Exception as e:
        raise ValueError(f"Error extracting message from image: {str(e)}")


def display_image_encryption():
    st.header(" Image Pass🔒")
    st.subheader("What can this tool do?")
    st.write("Upload an image, input your password, and let our tool seamlessly embed it into the image. Keep your passwords private with our intuitive and secure steganography solution. Start encoding and decoding hidden passwords now!!")
    st.write("You can make it better. Give suggestions below :smile:")
    st.write("---")
    st.subheader("Choose an option: ")
    encryption_choice = st.radio("options:", ["Encryption", "Decryption"])

    if encryption_choice == "Encryption":
        st.subheader("Encryption")
        message_to_encode = st.text_input("Enter Message:", placeholder="Type your secret message here...")
        image_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"], help="Upload the image you want to use for encoding the message")

        if st.button("Encrypt"):
            if not message_to_encode or not image_file:
                st.error("Please enter a message and upload an image.")
            else:
                try:
                    encoded_image = encode_in_image(image_file, message_to_encode)
                    st.image(encoded_image, caption="Encoded Image", use_column_width=True)

                    img_byte_arr = io.BytesIO()
                    encoded_image.save(img_byte_arr, format='PNG')  # Save as PNG
                    img_byte_arr = img_byte_arr.getvalue()

                    st.success("Message encoded successfully. Download the image using the button below.")
                    st.download_button("Download Encoded Image", data=img_byte_arr, file_name="encoded_image.png", mime="image/png")
                except Exception as e:
                    st.error(f"Error during encryption: {str(e)}")

    elif encryption_choice == "Decryption":
        st.subheader("Decryption")
        encrypted_image_file = st.file_uploader("Upload Encrypted Image", type=["png", "jpg", "jpeg"], help="Upload the image containing the hidden message")

        if st.button("Decrypt"):
            if not encrypted_image_file:
                st.error("Please upload an encrypted image.")
            else:
                try:
                    decoded_message = extract_from_image(encrypted_image_file)
                    st.success("Message decoded successfully.")
                    st.text_area("Decoded Message:", value=decoded_message, height=200)
                except Exception as e:
                    st.error(f"Error during decryption: {str(e)}")

# Display the main page (Image Encryption)
display_image_encryption()

# Display the form
st.write("---")
st.header("💬 What are your thoughts about this tool?")
contact_form = """
<form action="https://formsubmit.co/umerfarooq230@email.com" method="POST">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your Email" required>
    <textarea name="message" placeholder="Your message" required></textarea>
    <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

# Add footer
footer = """
<div class="footer">
    <p>&copy; 2024 <i class="fas fa-lock"></i> All rights reserved.</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)

# Load Font Awesome
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
""", unsafe_allow_html=True)

# Add Google Analytics
st.markdown("""
<script async src="https://www.googletagmanager.com/gtag/js?id=G-1X0J3BNNZL"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-1X0J3BNNZL');
</script>
""", unsafe_allow_html=True)
