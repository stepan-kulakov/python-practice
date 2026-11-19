def c_to_f(celsius: float) -> float:
    """Convert degrees Celsius to degrees Fahrenheit."""
    return celsius * 9 / 5 + 32


def f_to_c(fahrenheit: float) -> float:
    """Convert degrees Fahrenheit to degrees Celsius."""
    return (fahrenheit - 32) * 5 / 9


def read_number(prompt: str) -> float:
    """Ask until the user enters a valid number."""
    while True:
        raw = input(prompt).strip().replace(",", ".")
        try:
            return float(raw)
        except ValueError:
            print("That is not a number, try again.")


def main() -> None:
    while True:
        print()
        print("Temperature converter")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Quit")
        choice = input("Choose 1, 2 or 3: ").strip()

        if choice == "1":
            value = read_number("Enter temperature in C: ")
            print(f"{value:.1f} C = {c_to_f(value):.1f} F")
        elif choice == "2":
            value = read_number("Enter temperature in F: ")
            print(f"{value:.1f} F = {f_to_c(value):.1f} C")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, enter 1, 2 or 3.")


if __name__ == "__main__":
    main()