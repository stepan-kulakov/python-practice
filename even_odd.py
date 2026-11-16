def is_even(number: int) -> bool:
    """Return True if the number is even."""
    return number % 2 == 0


def main() -> None:
    while True:
        raw = input("Enter an integer: ").strip()
        try:
            number = int(raw)
            break
        except ValueError:
            print("That is not an integer, try again.")

    if is_even(number):
        print(f"{number} is even")
    else:
        print(f"{number} is odd")


if __name__ == "__main__":
    main()