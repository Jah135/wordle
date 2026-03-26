from .game import LetterValidity, Guess
from pyansi import AnsiStyle, Palette, PaletteColor

NEUTRAL_STYLE = AnsiStyle(
    fg=Palette(PaletteColor.Black), bg=Palette(PaletteColor.White)
)
CORRECT_STYLE = AnsiStyle(
    fg=Palette(PaletteColor.Black), bg=Palette(PaletteColor.BrightGreen)
)
EXISTS_STYLE = AnsiStyle(
    fg=Palette(PaletteColor.Black), bg=Palette(PaletteColor.BrightYellow)
)
INCORRECT_STYLE = AnsiStyle(
    fg=Palette(PaletteColor.Black), bg=(Palette(PaletteColor.BrightBlack))
)


def format_letter(char: str, validity: LetterValidity | None = None) -> str:
    display = f" {char.upper()} "
    if validity == None:
        return NEUTRAL_STYLE.apply_with_reset(display)
    elif validity == LetterValidity.Correct:
        return CORRECT_STYLE.apply_with_reset(display)
    elif validity == LetterValidity.Exists:
        return EXISTS_STYLE.apply_with_reset(display)
    return INCORRECT_STYLE.apply_with_reset(display)


def format_guess(guess: Guess) -> str:
    return "".join(format_letter(char, validity) for char, validity in zip(*guess))
