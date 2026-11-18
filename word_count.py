import string
from pathlib import Path


def count_words(path: str) -> dict[str, int]:
    """Count how many times each word appears in a text file."""
    text = Path(path).read_text(encoding="utf-8").lower()
    counts: dict[str, int] = {}
    for word in text.split():
        word = word.strip(string.punctuation)
        if word:
            counts[word] = counts.get(word, 0) + 1
    return counts


def top_words(counts: dict[str, int], n: int = 10) -> list[tuple[str, int]]:
    """Return the n most common words as (word, count) pairs."""
    return sorted(counts.items(), key=lambda item: item[1], reverse=True)[:n]


def main() -> None:
    try:
        counts = count_words("text.txt")
    except FileNotFoundError:
        print("File text.txt not found. Create it next to this script.")
        return

    for word, number in top_words(counts):
        print(f"{word}: {number}")


if __name__ == "__main__":
    main()