"""Get the meanings of all words in 'words.txt' and save to JSON."""

import concurrent.futures
import json

from PyDictionary import PyDictionary
from tqdm import tqdm

dictionary = PyDictionary()


def get_meaning(term: str):
    return (term, dictionary.meaning(term))


def main():
    with open("words.txt") as f:
        words = [line.strip() for line in f]

    print(f"Gettings meanings of {len(words):,} words")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        meanings = dict(tqdm(executor.map(get_meaning, words), total=len(words)))

    with open("meanings.json", "w") as f:
        json.dump(meanings, f)


if __name__ == "__main__":
    main()
