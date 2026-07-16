#!/usr/bin/env python3

def	input_temperature(temp_str):
	value = int(temp_str)
	return value

def	test_temperature():
	inputs = ["25", "abc"]
	for i in inputs:
		print(f"Input data is '{i}'")
		try:
			value = input_temperature(i)
			print(f"Temperature is now {value}°C\n")
		except ValueError as e:
			print(f"caugh input_temperature error: {e}\n")
	
	print("All tests completed — program didn't crash")


def	main():
	print("=== Garden Temperature\n")
	test_temperature()

if	__name__ == "__main__":
	main()