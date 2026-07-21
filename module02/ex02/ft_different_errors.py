#!/usr/bin/env python3

def	garden_operations(operation_number):
	if operation_number == 0:
		k = int("abc")
	elif operation_number == 1:
		k = 2 / 0
	elif operation_number == 2:
		file = open("tchi.txt")
	elif operation_number == 3:
		k  = "testing operation" + 3

def	test_error_types():
	for i in range (4):
		print(f"testing operation {i}...")
		try:
			garden_operations(i)
		except Exception as err:
			print(f"Caught {err.__class__.__name__}: {err}")
	
	print("\nAll error types tested successfully!")

def	main():
	print("=== Garden Error Types Demo ===")
	test_error_types()

if __name__ == "__main__":
	main()