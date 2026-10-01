from __future__ import annotations

import re
from collections import Counter


class TextAnalyzer:
    """Utilities for counting words, sentences, and ranking keywords."""

    @staticmethod
    def tokenize(text: str) -> list[str]:
        return re.findall(r"\b[\w'-]+\b", text.lower())

    @staticmethod
    def word_count(text: str) -> int:
        return len(TextAnalyzer.tokenize(text))

    @staticmethod
    def sentence_count(text: str) -> int:
        sentences = [segment for segment in re.split(r"[.!?]+", text) if segment.strip()]
        return len(sentences)

    @staticmethod
    def top_keywords(text: str, top_n: int = 20, stopwords: list[str] | None = None) -> list[str]:
        tokens = TextAnalyzer.tokenize(text)
        if stopwords:
            stop_words = {word.lower() for word in stopwords}
            tokens = [token for token in tokens if token not in stop_words]

        counts = Counter(tokens)
        return [word for word, _ in counts.most_common(top_n)]

    @staticmethod
    def summary(text: str, top_n: int = 5, stopwords: list[str] | None = None) -> dict[str, object]:
        return {
            "word_count": TextAnalyzer.word_count(text),
            "sentence_count": TextAnalyzer.sentence_count(text),
            "top_keywords": TextAnalyzer.top_keywords(text, top_n=top_n, stopwords=stopwords),
        }
