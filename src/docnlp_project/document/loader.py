from __future__ import annotations

from pathlib import Path


class DocumentLoader:
    """Load documents from a folder and return their content as structured records."""

    SUPPORTED_EXTENSIONS = {".txt", ".md", ".csv", ".json", ".docx"}

    def load_text(self, file_path: str) -> str:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"Document not found: {file_path}")

        if path.suffix.lower() == ".docx":
            return self._load_docx(str(path))

        return path.read_text(encoding="utf-8")

    def _load_docx(self, file_path: str) -> str:
        from docx import Document

        doc = Document(file_path)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return "\n".join(full_text)

    def process_file(self, file_path: str | Path, records: list[dict[str, str]]) -> list[dict[str, str]]:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"Document not found: {file_path}")

        if path.is_file() and path.suffix.lower() in self.SUPPORTED_EXTENSIONS:
            records.append(
                {
                    "file_name": path.name,
                    "file_path": str(path),
                    "content": self.load_text(str(path)),
                }
            )

        return records

    def load_directory(self, directory: str | Path) -> list[dict[str, str]]:
        directory_path = Path(directory)

        if directory_path.is_file():
            return self.process_file(directory_path, [])

        if not directory_path.exists() or not directory_path.is_dir():
            raise FileNotFoundError(f"Directory not found: {directory}")

        records: list[dict[str, str]] = []
        for file_path in sorted(directory_path.iterdir()):
            if file_path.is_file() and file_path.suffix.lower() in self.SUPPORTED_EXTENSIONS:
                self.process_file(file_path, records)

        return records
