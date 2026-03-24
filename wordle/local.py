from .game import WordleGame, LetterValidity
from .player import WordlePlayer


def check_word(guess: str, secret: str) -> list[LetterValidity]:
    available_counts = {char: secret.count(char) for char in guess}
    exists = {}

    for secret_char, guess_char in zip(secret, guess):
        if guess_char == secret_char:
            available_counts[guess_char] -= 1
        if guess_char in secret:
            exists[guess_char] = True

    word_validity = []

    for secret_char, guess_char in zip(secret, guess):
        if secret_char == guess_char:
            word_validity.append(LetterValidity.Correct)
            continue

        exists_in_remaining_secret = available_counts[guess_char] > 0
        available_counts[guess_char] -= 1

        if exists_in_remaining_secret:
            word_validity.append(LetterValidity.Exists)
        else:
            word_validity.append(
                LetterValidity.Incorrect
                if exists.get(guess_char, False) == False
                else LetterValidity.TooMany
            )

    return word_validity


class LocalWordleGame(WordleGame):
    def __init__(self, secret_word: str, max_guesses: int = 6) -> None:
        self.secret_word = secret_word.casefold()
        self.max_guesses = max_guesses
        self.is_done = False
        self.is_win = False
        self.guess_history: list[tuple[str, list[LetterValidity]]] = []

    def make_guess(self, word: str) -> tuple[str, list[LetterValidity]]:
        caseless_word = word.casefold()

        guess_info = (caseless_word, check_word(caseless_word, self.secret_word))
        self.guess_history.append(guess_info)

        self.is_win = caseless_word == self.secret_word
        self.is_done = self.is_win or (len(self.guess_history) >= self.max_guesses)

        return guess_info

    def reset(self):
        self.is_done = False
        self.is_win = False
        self.guess_history.clear()


class LocalWordlePlayer(WordlePlayer):
    def prompt_word(self) -> str:
        return input("> ")
