"""Make CSV of words and meanings. This CSV can be imported into Anki."""

import json
import pandas as pd


def main():
    with open("meanings.json") as f:
        all_meanings = json.load(f)

    data = []
    for word, parts_of_speech in all_meanings.items():
        if parts_of_speech is None:
            continue
        answer = ""
        for pos in sorted(parts_of_speech.keys()):
            meanings = parts_of_speech[pos]
            answer += f"<i>{pos.title()}:</i>"
            answer += "<ul>"
            for meaning in meanings:
                answer += f"<li>{meaning}</li>"
            answer += "</ul>"
            answer += "<br/>"
        data.append({"Front": word, "Back": answer})

    pd.DataFrame(data).to_csv("words_meanings.csv", index=False)


if __name__ == "__main__":
    main()
