import sys
import math


def is_prime(n: int) -> bool:
	if n <= 1:
		return False
	if n <= 3:
		return True
	if n % 2 == 0:
		return False
	limit = math.isqrt(n)
	for i in range(3, limit + 1, 2):
		if n % i == 0:
			return False
	return True


def _print_result(n: int) -> None:
	if is_prime(n):
		print(f"{n} is prime")
	else:
		print(f"{n} is not prime")


if __name__ == "__main__":
	if len(sys.argv) > 1:
		for token in sys.argv[1:]:
			try:
				val = int(token)
			except ValueError:
				print(f"'{token}' is not an integer")
				continue
			_print_result(val)
	else:
		try:
			s = input("Enter an integer: ")
			n = int(s.strip())
		except ValueError:
			print("Please enter a valid integer")
		else:
			_print_result(n)

