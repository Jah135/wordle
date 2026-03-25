from .game import LetterValidity


def get_word_validity(guess: str, secret: str) -> list[LetterValidity]:
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
