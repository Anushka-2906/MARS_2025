# MARS 2025 – Automated Metadata Generation System

This project presents a web-based system that automatically generates structured metadata from unstructured documents. It supports `.txt`, `.pdf`, and `.docx` formats, and incorporates OCR (Optical Character Recognition) for scanned or image-based PDFs. The system runs seamlessly on **Google Colab** and includes a clean, pastel-themed web interface.

---

## Project Overview

As unstructured documents become more prevalent, automating metadata generation is critical for indexing, classification, and retrieval. This system extracts meaningful content from documents and outputs it as structured JSON metadata, ideal for content management and digital archiving workflows.

---

## Features

- **Automated Metadata Extraction**  
  Generates metadata including title, word count, keywords, summary, language, file type, and upload time.

- **Multi-format Document Support**  
  Accepts `.txt`, `.docx`, and `.pdf` files. OCR is used for image-based PDFs.

- **Semantic Analysis**  
  Identifies and summarizes key sentences and topics using lightweight NLP.

- **Structured JSON Output**  
  Outputs metadata in a clean, structured format for further use or integration.

- **Web Interface**  
  Users can upload documents and view metadata through a simple pastel-themed UI.

- **Google Colab Compatible**  
  Fully runnable in Google Colab with `flask-ngrok` for live public access.

---

## Folder Structure

```
MARS_2025/
├── app.py                        ← Flask backend (optional)
├── MARS.ipynb                    ← Google Colab notebook (fully runnable ✅)
├── templates/
│   └── index.html               ← Upload form with pastel styling
├── static/
│   └── bg.avif                  ← Background image used in the UI
├── uploads/                     ← Created at runtime (ignored in repo)
├── output/                      ← Created at runtime (ignored in repo)
├── README.md                    ← Project documentation
└── demo.mp4 / demo_link.txt     ← Optional 2-minute usage demo
```

> Note: `uploads/` and `output/` are temporary runtime folders and need not be pushed to GitHub.

---

## How to Run (Google Colab – Recommended)

1. Open the notebook [`MARS.ipynb`](https://github.com/Anushka-2906/MARS_2025/blob/main/MARS.ipynb) in [Google Colab](https://colab.research.google.com).
2. Run all the cells sequentially.
3. A public ngrok URL will be generated.
4. Upload any `.txt`, `.pdf`, or `.docx` file using the interface.
5. View and download the generated metadata as a JSON file.

---

## Optional: Local Setup

1. Clone the repository:

```bash
git clone https://github.com/Anushka-2906/MARS_2025.git
cd MARS_2025
```

2. Install required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python app.py
```

4. Open `http://localhost:5000` in your browser.

---

## Sample Metadata Output

```json
{
  "filename": "example.pdf",
  "title": "Fundamentals of Operating Systems",
  "word_count": 1482,
  "keywords": ["operating systems", "memory", "process", "scheduling"],
  "summary": "This document introduces the key principles of operating systems...",
  "language": "en",
  "created_time": "2025-06-22T13:40:12",
  "file_type": "application/pdf"
}
```

---

## Deliverables

- ✅ `MARS.ipynb` — Executable Google Colab notebook
- ✅ `index.html` with pastel upload form
- ✅ `README.md` — Setup and usage instructions
- ⏯️ `demo.mp4` or `demo_link.txt` — Optional demo showing end-to-end flow

---


