import streamlit as st
from PIL import Image
import pytesseract
import os

# Optional: Specify tesseract path for Windows
# Uncomment and update the path if needed
pytesseract.pytesseract.tesseract_cmd = r'D:\Software\Tesseract\tesseract.exe'

st.set_page_config(page_title="OCR Text Extractor", layout="centered")

st.title("📄 OCR Text Extractor")
st.write("Upload an image to extract text using OCR (Tesseract)")

# File uploader
uploaded_file = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    try:
        # Load image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # OCR Processing
        with st.spinner("Extracting text..."):
            extracted_text = pytesseract.image_to_string(image)

        st.subheader("📌 Extracted Text:")
        st.text_area("Text Output", extracted_text.strip(), height=300)

    except Exception as e:
        st.error(f"❌ An error occurred: {str(e)}")