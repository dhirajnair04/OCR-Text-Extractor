# 📄 OCR Text Extractor

A simple and effective web-based **OCR (Optical Character Recognition)** app that extracts text from uploaded images using **Tesseract OCR** and `Streamlit`. Supports PNG, JPG, and JPEG formats for fast, local text detection from image content.

---

## 🚀 Features

- 📤 Upload image files (PNG, JPG, JPEG)
- 🔍 Extract printed or handwritten text using Tesseract OCR
- 💬 View extracted text instantly in the browser
- ⚡ Fast and lightweight Streamlit interface
- 🖼️ Displays the uploaded image alongside results

---

## 🧠 How It Works

1. User uploads an image via the Streamlit app.
2. The image is displayed for visual confirmation.
3. The app uses `pytesseract` (Python wrapper for Tesseract) to extract text.
4. The extracted text is displayed in a scrollable text box.

---

## 🛠️ Tech Stack

- `Python 3.9+`
- `Streamlit`
- `Pillow (PIL)`
- `pytesseract` (Tesseract OCR backend)

---

## 📂 Project Structure

```
📦 project-root/
├── 📄 app2.py # Main Streamlit application
├── 📄 requirements.txt # required libraries to run the app
└── 📄 README.md # Project documentation
```

---

## 📌 Tesseract Setup (Windows)

Make sure you have [Tesseract OCR installed](https://github.com/tesseract-ocr/tesseract). Then in your script:

```python
pytesseract.pytesseract.tesseract_cmd = r'D:\Software\Tesseract\tesseract.exe'
```

---

## ▶️ Run the App

```
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch Streamlit app
streamlit run ocr_app.py
```

---

## 📌 Use Cases

- Reading printed documents from photos
- Quick digitization of paper text
- Scanning handwritten notes (depending on clarity)

---

## 📜 License

This project is open-source under the MIT License. Feel free to use, share, and build on it!
