# Advanced Automated Metadata Generation System

import os
import fitz  # PyMuPDF for PDFs
import docx
import pytesseract
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
from werkzeug.utils import secure_filename
from flask import Flask, request, render_template, jsonify, send_file
import re
from langdetect import detect, DetectorFactory
from datetime import datetime
import mimetypes
from collections import Counter
import json

# Ensure consistent language detection results
DetectorFactory.seed = 0

# Optional: set path to tesseract.exe (Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

# Utility: Clean text

def clean_text(text):
    return re.sub(r'\s+', ' ', text.strip())

# Extract text based on file type

def extract_text_pdf(file_path):
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_text_docx(file_path):
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def extract_text_image(file_path):
    image = Image.open(file_path)
    image = image.resize((image.width * 2, image.height * 2), Image.LANCZOS)
    gray = ImageOps.grayscale(image)
    sharp = gray.filter(ImageFilter.SHARPEN)
    contrast = ImageEnhance.Contrast(sharp).enhance(3)
    return pytesseract.image_to_string(contrast, config='--psm 4')

# Semantic content: enhanced for image-based inputs

def extract_semantic_content(text):
    lines = text.split('\n')
    clean_lines = [line.strip() for line in lines if line.strip()]
    if len(clean_lines) == 0:
        return ""
    elif len(clean_lines) == 1:
        return clean_lines[0]
    elif len(clean_lines) == 2:
        return clean_lines[0] + " " + clean_lines[1]
    else:
        return " ".join(clean_lines[:min(6, len(clean_lines))])

# Keyword extractor (frequency-based)

def extract_keywords(text, top_n=10):
    words = re.findall(r'\b[a-zA-Z]{5,}\b', text.lower())
    freq = Counter(words)
    return [word for word, _ in freq.most_common(top_n)]

# Metadata Generator

def generate_metadata(text, filename):
    lines = text.split('\n')
    clean_lines = [line.strip() for line in lines if line.strip()]
    title = clean_lines[0] if clean_lines else "Untitled"
    word_count = len(re.findall(r'\w+', text))
    keywords = extract_keywords(text)
    semantic_summary = extract_semantic_content(text)
    try:
        language = detect(text) if len(text) > 20 else "unknown"
    except:
        language = "unknown"
    created_time = datetime.now().isoformat()
    file_type, _ = mimetypes.guess_type(filename)

    metadata = {
        "filename": filename,
        "title": title[:100],
        "word_count": word_count,
        "keywords": keywords,
        "summary": semantic_summary,
        "language": language,
        "created_time": created_time,
        "file_type": file_type or "unknown"
    }
    return metadata

# Flask Routes
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        ext = filename.lower().split('.')[-1]
        if ext == 'pdf':
            text = extract_text_pdf(file_path)
        elif ext == 'docx':
            text = extract_text_docx(file_path)
        elif ext == 'txt':
            text = extract_text_txt(file_path)
        elif ext in ['png', 'jpg', 'jpeg']:
            text = extract_text_image(file_path)
        else:
            return "Unsupported file type."

        metadata = generate_metadata(text, filename)

        output_path = os.path.join(app.config['OUTPUT_FOLDER'], filename + '_metadata.json')
        with open(output_path, 'w', encoding='utf-8') as out_file:
            json.dump(metadata, out_file, indent=4)

        return jsonify(metadata)

@app.route('/download/<filename>')
def download_metadata(filename):
    filepath = os.path.join(app.config['OUTPUT_FOLDER'], filename + '_metadata.json')
    return send_file(filepath, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
