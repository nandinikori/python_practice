from pathlib import Path

from docnlp_project import DocumentLoader, DocumentPreprocessor, TextAnalyzer


if __name__ == "__main__":
    data_dir = Path(__file__).resolve().parents[1] / "data"

    loader = DocumentLoader()
    documents = loader.load_directory(str(data_dir)) if data_dir.exists() else []

    if not documents:
        print("No documents found in data/. Add .txt or .md files to explore the pipeline.")
    else:
        clean_text = DocumentPreprocessor.normalize_whitespace(documents[0]["content"])
        summary = TextAnalyzer.summary(clean_text)

        print(f"Loaded document: {documents[0]['file_name']}")
        print(summary)
