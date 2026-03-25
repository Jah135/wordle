from enum import IntEnum


class LetterValidity(IntEnum):
    Incorrect = 0
    TooMany = 1
    Exists = 2
    Correct = 4


Guess = tuple[str, list[LetterValidity]]


class WordleGame:
    is_done: bool = False
    is_won: bool = False
    guess_history: list[Guess]

    def __init__(self) -> None:
        self.guess_history = []

    def check_validity(self, word: str) -> list[LetterValidity]: ...
    def check_is_done(self, word: str) -> bool: ...
    def check_is_won(self, word: str) -> bool: ...
    def make_guess(self, word: str) -> Guess:
        guess = (word, self.check_validity(word=word))
        self.guess_history.append(guess)

        return guess
