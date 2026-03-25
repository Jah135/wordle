from enum import IntEnum


class LetterValidity(IntEnum):
    Incorrect = 0
    TooMany = 1
    Exists = 2
    Correct = 4


Guess = tuple[str, list[LetterValidity]]


class WordleGame:
    guess_history: list[Guess]

    def __init__(self) -> None:
        self.guess_history = []

    @property
    def is_done(self) -> bool: ...
    @property
    def is_won(self) -> bool: ...

    def check_validity(self, word: str) -> list[LetterValidity]: ...
    def make_guess(self, word: str) -> Guess:
        guess = (word, self.check_validity(word=word))
        self.guess_history.append(guess)

        return guess
