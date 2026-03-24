from enum import Enum


class LetterValidity(Enum):
    TooMany = "toomany"
    Incorrect = "incorrect"
    Exists = "exists"
    Correct = "correct"


class WordleGame:
    def make_guess(self, word: str) -> tuple[str, list[LetterValidity]]: ...
