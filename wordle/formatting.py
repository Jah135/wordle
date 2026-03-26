def format_letter(char: str, validity: LetterValidity | None = None) -> str:
    display = f" {char.upper()} "
    if validity == None:
        return NEUTRAL_STYLE.apply_with_reset(display)
    elif validity == LetterValidity.Correct:
        return CORRECT_STYLE.apply_with_reset(display)
    elif validity == LetterValidity.Exists:
        return EXISTS_STYLE.apply_with_reset(display)
    return INCORRECT_STYLE.apply_with_reset(display)


def format_guess(guess: str, guess_validity: list[LetterValidity]) -> str:
    return "".join(
        format_letter(char, validity) for char, validity in zip(guess, guess_validity)
    )
