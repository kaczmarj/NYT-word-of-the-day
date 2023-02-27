"""Get the meanings of all words in 'words.txt' and save to JSON."""

import json

from PyDictionary import PyDictionary


def main():
    with open("words.txt") as f:
        words = [line.strip() for line in f]

    print(len(words), "words")
    dictionary = PyDictionary(words)
    meanings = dictionary.getMeanings()

    with open("meanings.json", "w") as f:
        json.dump(meanings, f)


if __name__ == "__main__":
    main()
