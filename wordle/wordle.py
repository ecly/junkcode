"""Small script for finding optimal word combinations for wordle.

In this case we define optimal as 5 words with no overlapping characters
yielding a total coverage of 25 characters after the 5 words.

The script has an added element of randomness, by allowing it to sometimes
choose a suboptimal word, so rerunning the script multiple times can yield
different answers.

Developed specifically for the Dansk Sprognævn's Danish word lists found at:
    https://dsn.dk/ordboeger/retskrivningsordbogen/ro-elektronisk-og-som-bog/

With a direct download link at:
    https://dsn.dk/wp-content/uploads/2021/03/RO2012.opslagsord.med_.homnr_.og_.ordklasse.zip


Usage:
    `python3 wordle.py`
"""
import random
import re


def get_all_5_unique_letter_words():
    with open("wordlist_DK.txt") as file:
        words = [line.split(";")[0] for line in file]
        words = [word for word in words if re.match(r"^([a-zæøå]){5}$", word)]
        words = [w for w in words if len(set(w)) == 5]

    return words


def get_word_weight(words, word):
    """Get the weight of the `word` defined as amount of `words` with purely disjoint characters to `word`."""
    weight = 0
    for w in words:
        if not any(c in word for c in w):
            weight += 1

    return weight


def choose_word(words):
    """Choose a next word form words based on `get_word_weight` and some randomness."""
    words_with_weight = sorted([(get_word_weight(words, word), word) for word in words])

    # this is a bit arbitrarily chosen, but allows selecting non-optimal words
    lower_weight_offset = max(1, len(words_with_weight) // 300)
    best_weight, _ = words_with_weight[-lower_weight_offset]
    all_best = [word for weight, word in words_with_weight if weight >= best_weight]
    return random.choice(all_best)


def get_n_best_word_choices(words: list[str], n: int = 5) -> list[str]:
    seen_characters = set()
    chosen_words = []
    while len(chosen_words) < n:
        word = choose_word(words)
        seen_characters.update(list(word))
        chosen_words.append(word)

        words = [w for w in words if not any(c in word for c in w)]
        if not words:
            break

    return chosen_words


def main():
    words = get_all_5_unique_letter_words()
    chosen_words = get_n_best_word_choices(words)
    seen_characters = {c for word in chosen_words for c in word}
    print(f"Used characters {len(seen_characters)}: {''.join(sorted(seen_characters))}")
    print("Chosen words:", *chosen_words)


if __name__ == "__main__":
    main()
