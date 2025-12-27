import sys
import re


def is_palindrome(s: str) -> bool:
	"""Return True if string `s` is a palindrome.

	Non-alphanumeric characters are ignored and comparison is case-insensitive.
	"""
	cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
	return cleaned == cleaned[::-1]


def _print_result(s: str) -> None:
	if is_palindrome(s):
		print(f"'{s}' is a palindrome")
	else:
		print(f"'{s}' is not a palindrome")


if __name__ == "__main__":
	if len(sys.argv) > 1:
		for token in sys.argv[1:]:
			_print_result(token)
	else:
		try:
			s = input("Enter a word or phrase: ")
		except EOFError:
			sys.exit(0)
		_print_result(s)

