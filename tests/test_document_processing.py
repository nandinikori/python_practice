from docnlp_project import DocumentLoader, DocumentPreprocessor, TextAnalyzer


def test_document_loader_reads_txt_files(tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("Hello world! This is a sample document.", encoding="utf-8")

    loader = DocumentLoader()
    records = loader.load_directory(str(tmp_path))

    assert len(records) == 1
    assert records[0]["file_name"] == "sample.txt"
    assert "Hello world" in records[0]["content"]


def test_document_loader_reads_single_file(tmp_path):
    file_path = tmp_path / "single.txt"
    file_path.write_text("Single file test content.", encoding="utf-8")

    loader = DocumentLoader()
    records = loader.load_directory(str(file_path))

    assert len(records) == 1
    assert records[0]["file_name"] == "single.txt"
    assert "Single file test" in records[0]["content"]


def test_preprocessor_normalizes_text():
    text = "  Hello   WORLD!!!  This   is   text.  "

    cleaned = DocumentPreprocessor.normalize_whitespace(text)
    tokens = DocumentPreprocessor.tokenize(cleaned)

    assert cleaned == "Hello WORLD!!! This is text."
    assert tokens[0] == "Hello"
    assert tokens[-1] == "text."


def test_text_analyzer_summarizes_content():
    text = "NLP helps process documents. NLP extracts insights and organizes text."

    summary = TextAnalyzer.summary(text)

    assert summary["word_count"] == 10
    assert summary["sentence_count"] == 2
    assert "nlp" in summary["top_keywords"]
