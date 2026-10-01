from __future__ import annotations

import re


class DocumentPreprocessor:
    """Basic text cleaning and tokenization utilities."""

    @staticmethod
    def normalize_whitespace(text: str) -> str:
        return re.sub(r"\s+", " ", text).strip()

    @staticmethod
    def remove_punctuation(text: str, replacement: str = " ") -> str:
        return re.sub(r"[^\w\s]", replacement, text)

    @staticmethod
    def tokenize(text: str) -> list[str]:
        return DocumentPreprocessor.normalize_whitespace(text).split()
