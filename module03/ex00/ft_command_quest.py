#! /usr/bin/env python3

import sys

def	calc_arguments() -> None:
	print("Program name:", sys.argv[0])

	if len(sys.argv) == 1:
		print("No argument provided!")
	else:
		print("Arguments received:", len(sys.argv) - 1)
		for pos in range(len(sys.argv) - 1):
			print(f"Argument {pos + 1}: {sys.argv[pos + 1]}")
	print(f"Total arguments: {len(sys.argv)}")

def	main() -> None:
	calc_arguments()

if __name__ == "__main__":
	main()