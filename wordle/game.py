from enum import IntEnum

class LetterValidity(IntEnum):
    Incorrect = 0
    TooMany = 1
    Exists = 2
    Correct = 4

class WordleGame:
    def make_guess(self, word: str) -> tuple[str, list[LetterValidity]]: ...
