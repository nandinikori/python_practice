# Document NLP Project

This repository is a starter library for building document processing and natural language processing (NLP) workflows. It provides a clean package structure, reusable text-processing utilities, and a foundation for adding document analysis capabilities.

## Why this structure

- Keeps document ingestion and preprocessing separate from analysis code
- Makes it easy to add PDF, DOCX, or OCR capabilities later
- Supports a project focused on text extraction, cleaning, keyword analysis, and semantic retrieval
- Uses a standard Python package layout for packaging and testing

## Project structure

- `src/docnlp_project/document/` — file loading and text cleaning
- `src/docnlp_project/nlp/` — word and keyword analysis
- `tests/` — validation for the core library behavior
- `docs/roadmap.md` — suggested growth path for the project

## Quick start

```bash
pip install -e .
```

```python
from docnlp_project import DocumentLoader, DocumentPreprocessor, TextAnalyzer

loader = DocumentLoader()
records = loader.load_directory("data")
text = records[0]["content"]
cleaned = DocumentPreprocessor.normalize_whitespace(text)
summary = TextAnalyzer.summary(cleaned)

print(summary)
```

## Recommended next steps

1. Add PDF and Scanned images in JPG and scanned pdf file  loaders
2. Create a preprocessing pipeline with stopwords and lemmatization
3. Add keyword extraction, summarization, and topic modeling
4. Build a mini retrieval or search application for document collections
5. Package the best demo into a polished project showcase
