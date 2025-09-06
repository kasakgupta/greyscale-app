import io
from PIL import Image
import numpy as np
import cv2
import streamlit as st

# Page setup
st.set_page_config(page_title="Grayscale Converter", page_icon="🎨", layout="wide")
st.title("🎨 Image Grayscale Converter")
st.write("Upload an image and instantly get a grayscale version.")

# File uploader
uploaded_file = st.file_uploader("Upload an image (jpg, png)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    img_array = np.array(image)

    # Convert to grayscale
    gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)

    # Display side by side
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Original")
        st.image(image, width=300)
    with col2:
        st.subheader("Grayscale")
        st.image(gray, width=300, channels="GRAY")

    # Download button
    gray_pil = Image.fromarray(gray)
    buf = io.BytesIO()
    gray_pil.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        label="📥 Download Grayscale Image",
        data=byte_im,
        file_name="grayscale.png",
        mime="image/png"
    )
else:
    st.info("Upload an image to get started.")
