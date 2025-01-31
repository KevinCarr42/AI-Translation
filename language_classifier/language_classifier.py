import json
from pathlib import Path


class LanguageClassifier:
    def __init__(self, wordlist_path: str = None):
        default_path = Path(__file__).parent / "wordlists.json"
        wordlist_path = wordlist_path or default_path

        with open(wordlist_path, "r", encoding="utf-8") as f:
            wordlists = json.load(f)

        self.french_words = set(wordlists["fr"])
        self.english_words = set(wordlists["en"])

    def classify(self, sentence, tolerance=1):
        words = sentence.lower().split()
        en_count = sum(1 for word in words if word in self.english_words)
        fr_count = sum(1 for word in words if word in self.french_words)

        if en_count > 0 and fr_count <= tolerance:
            return 'en'
        if fr_count > 0 and en_count <= tolerance:
            return 'fr'
        if fr_count > tolerance and en_count > tolerance:
            return 'mixed'
        return 'unknown'
