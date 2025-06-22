# Automated Metadata Generation System

This project is a fully functional web-based system that automatically generates structured metadata from unstructured documents. It supports multiple formats including TXT, PDF, and DOCX, and incorporates OCR to handle scanned or image-based files.

## Project Overview

This system aims to simplify the process of metadata generation for a wide range of unstructured documents. It extracts meaningful content from uploaded files and converts it into structured metadata in JSON format. The system can be used in contexts like digital archiving, content classification, and document indexing.

### Core Features

- **Automated Metadata Generation**  
  Generates metadata fields such as title, word count, keywords, summary, language, file type, and upload time.

- **Content Extraction**  
  Supports `.txt`, `.pdf`, and `.docx` formats. For scanned PDFs or image-based documents, the system uses OCR to extract text content.

- **Semantic Content Identification**  
  Identifies and summarizes meaningful sections of the document using lightweight natural language processing.

- **Structured Metadata Output**  
  Outputs metadata in JSON format, which is easy to store, visualize, and integrate into other systems.

- **User Interface**  
  A clean web interface allows users to upload documents and view their metadata in real-time.

- **Google Colab Compatibility**  
  The system is fully runnable in Google Colab using `flask-ngrok`, making it easily accessible without requiring local setup.

---

## Folder Structure

```
automated_metadata/
├── app.py                        ← Flask backend (converted into notebook format)
├── automated_metadata.ipynb     ← Colab-compatible notebook (standalone and runnable)
├── templates/
│   └── index.html               ← Upload form (pastel-lavender theme)
├── static/
│   └── bg.avif                  ← Background image for the UI
├── uploads/                     ← Temporary folder created at runtime (ignored in repo)
├── output/                      ← Temporary folder created at runtime (ignored in repo)
├── README.md                    ← Project overview, setup, and usage instructions
└── demo.mp4 / demo_link.txt     ← Optional 2-minute demo (video or link)
```

> Note: The `uploads/` and `output/` folders are created dynamically and can be excluded from version control.

---

## How to Run (Google Colab)

1. Open `automated_metadata.ipynb` in Google Colab.
2. Run all the cells sequentially.
3. A public URL will be generated using ngrok.
4. Upload a document using the form.
5. The system will display metadata on the screen and save it in JSON format.

---

## Setup for Local Deployment (Optional)

1. Clone the repository:

```bash
git clone https://github.com/your-username/automated_metadata.git
cd automated_metadata
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

3. Run the Flask app:

```bash
python app.py
```

Then open `http://localhost:5000` in your browser.

---

## Deliverables

- `automated_metadata.ipynb` — Self-contained Colab notebook
- `templates/index.html` — Web interface with a pastel lavender theme
- `app.py` — Flask backend version (optional)
- `README.md` — Full documentation
- `demo.mp4` or `demo_link.txt` — Short demo video (optional)

---

## Example Output (JSON Metadata)

```json
{
  "filename": "sample.pdf",
  "title": "Introduction to Algorithms",
  "word_count": 1750,
  "keywords": ["algorithms", "complexity", "sorting"],
  "summary": "This document introduces fundamental algorithmic concepts...",
  "language": "en",
  "created_time": "2025-06-22T14:30:00",
  "file_type": "application/pdf"
}
```

---

