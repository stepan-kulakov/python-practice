def minimum(numbers: list[float]) -> float:
    """Return the smallest number in the list."""
    smallest = numbers[0]
    for n in numbers[1:]:
        if n < smallest:
            smallest = n
    return smallest


def maximum(numbers: list[float]) -> float:
    """Return the largest number in the list."""
    largest = numbers[0]
    for n in numbers[1:]:
        if n > largest:
            largest = n
    return largest


def average(numbers: list[float]) -> float:
    """Return the arithmetic mean of the list."""
    return sum(numbers) / len(numbers)


def read_numbers() -> list[float]:
    """Ask until the user enters at least one valid number."""
    while True:
        raw = input("Enter numbers separated by spaces: ").strip().replace(",", ".")
        parts = raw.split()
        if not parts:
            print("Please enter at least one number.")
            continue
        try:
            return [float(part) for part in parts]
        except ValueError:
            print("Only numbers are allowed, try again.")


def main() -> None:
    numbers = read_numbers()
    print(f"Count:   {len(numbers)}")
    print(f"Minimum: {minimum(numbers):.2f}")
    print(f"Maximum: {maximum(numbers):.2f}")
    print(f"Average: {average(numbers):.2f}")


if __name__ == "__main__":
    main()