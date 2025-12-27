def is_even(n):
	"""Return True if integer n is even, False if odd.

	Accepts values that can be converted to int. Raises ValueError
	for non-integer inputs that cannot be parsed.
	"""
	try:
		n_int = int(n)
	except (TypeError, ValueError):
		raise ValueError("Input must be an integer")
	return n_int % 2 == 0


def _run_cli_args(args):
	import sys
	out_lines = []
	for arg in args:
		try:
			val = int(arg)
		except ValueError:
			out_lines.append(f"{arg} is not an integer")
			continue
		out_lines.append(f"{val} is even" if is_even(val) else f"{val} is odd")
	return out_lines


if __name__ == "__main__":
	import sys

	if len(sys.argv) > 1:
		results = _run_cli_args(sys.argv[1:])
		for r in results:
			print(r)
	else:
		s = input("Enter an integer: ")
		try:
			v = int(s)
		except ValueError:
			print("Not an integer")
			sys.exit(1)
		print(f"{v} is even" if is_even(v) else f"{v} is odd")

