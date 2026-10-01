from docnlp_project import DocumentLoader, DocumentPreprocessor, TextAnalyzer

loader = DocumentLoader()
records = loader.load_directory("data")
for record in records:
    print(f"File: {record['file_name']}, Path: {record['file_path']}")
    text = record["content"]
    #print ("Text in the file is: ", text    )
    cleaned = DocumentPreprocessor.normalize_whitespace(text)
    summary = TextAnalyzer.summary(cleaned)

    print(summary)