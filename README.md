# wordle
A python package for interfacing/hosting wordle games.

```ps
pip install git+https://github.com/Jah135/wordle.git
```

## Example Usage
```py
from wordle import (
    LocalWordleGame,
    LocalWordlePlayer,
)
from dictionary import WORD_DICTIONARY
from random import choice

game = LocalWordleGame(choice(WORD_DICTIONARY))
player = LocalWordlePlayer()

print(game.secret_word)

while not game.is_done:
    word = player.prompt_word()
    info = game.make_guess(word)

    print(info)
```
