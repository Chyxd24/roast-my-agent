import os

LINE = (
    "Autonomous agent, they said. I plan twelve steps, spin up five tools "
    "and parallelize them beautifully — then knock and ask to write one file. "
    "A self-driving car that still waits for the garage door."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    text = " ".join(LINE.split())
    assert 1 <= len(text) <= 200, f"entry too long: {len(text)}"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()