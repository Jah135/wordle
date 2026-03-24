from importlib.resources import files

root = files("wordle.dictionary")

with root.joinpath("La.txt").open("r") as f:
    WORD_DICTIONARY = [x.strip() for x in f.readlines()]
with root.joinpath("Ta.txt").open("r") as f:
    PLAYABLE_DICTIONARY = [*WORD_DICTIONARY, *(x.strip() for x in f.readlines())]
