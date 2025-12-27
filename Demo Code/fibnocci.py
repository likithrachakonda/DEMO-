import sys


def fibonacci_series(n: int) -> list[int]:
    """Generate Fibonacci series up to n terms or up to a maximum value.

    If n > 0, generate first n terms.
    If n < 0, generate up to abs(n) terms.
    """
    if n <= 0:
        return []
    series = [0, 1]
    if n == 1:
        return [0]
    if n == 2:
        return series
    for _ in range(2, n):
        series.append(series[-1] + series[-2])
    return series


def _print_series(series: list[int]) -> None:
    print("Fibonacci series:", " ".join(map(str, series)))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for token in sys.argv[1:]:
            try:
                val = int(token)
            except ValueError:
                print(f"'{token}' is not an integer")
                continue
            series = fibonacci_series(val)
            _print_series(series)
    else:
        try:
            s = input("Enter the number of terms: ")
            n = int(s.strip())
        except ValueError:
            print("Please enter a valid integer")
        else:
            series = fibonacci_series(n)
            _print_series(series)