import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="Grayscale Converter", page_icon="🎨", layout="wide")

# Title & Description
st.title("🎨 Image Grayscale Converter")
st.write("Upload your image and instantly get a grayscale version.")

# Upload file
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read image
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    # Convert to grayscale
    gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)

    # Layout in 2 columns
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Original")
        st.image(image, width=400)
    with col2:
        st.subheader("Grayscale")
        st.image(gray, width = 400, channels="GRAY")

    # Download button
    result = Image.fromarray(gray)
    st.download_button(
        label="📥 Download Grayscale Image",
        data=result.tobytes(),
        file_name="grayscale.png",
        mime="image/png"
    )
