from .game import WordleGame, LetterValidity
from .player import WordlePlayer
from .utility import get_word_validity


class LocalWordleGame(WordleGame):
    def __init__(self, secret_word: str, max_guesses: int = 6) -> None:
        self.secret_word = secret_word.casefold()
        self.max_guesses = max_guesses
        self.guess_history: list[tuple[str, list[LetterValidity]]] = []

    @property
    def is_won(self) -> bool:
        if len(self.guess_history) == 0:
            return False
        return self.guess_history[-1][0] == self.secret_word

    @property
    def is_done(self) -> bool:
        return len(self.guess_history) >= self.max_guesses or self.is_won

    def check_validity(self, word: str) -> list[LetterValidity]:
        return get_word_validity(word, self.secret_word)

    def reset(self):
        self.guess_history.clear()


class LocalWordlePlayer(WordlePlayer):
    def prompt_word(self) -> str:
        return input("> ")
