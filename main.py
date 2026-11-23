"""Print the one-line roast stored in entry.txt.

The roast itself lives in entry.txt so the text judges see is exactly
the text this program prints. Nothing else is printed.
"""

from pathlib import Path


def load_roast() -> str:
    """Return the roast line, stripped of surrounding whitespace.

    Falls back to a short note if the entry file is missing or blank,
    so the program never prints nothing at all.
    """
    entry_path = Path(__file__).with_name("entry.txt")
    try:
        roast = entry_path.read_text(encoding="utf-8").strip()
    except (FileNotFoundError, OSError):
        roast = ""
    if not roast:
        roast = "(no roast written yet — see entry.txt)"
    return roast


def main() -> None:
    print(load_roast())


if __name__ == "__main__":
    main()
