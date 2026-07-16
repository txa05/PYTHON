#!/usr/bin/env python3

def	input_temperature(temp_str):
	value = int(temp_str)
	if value > 40:
		raise ValueError(f"{value}°C is too hot for plants (max 40°C)")
	if value < 0:
		raise ValueError(f"{value}°C is too cold for plants (min 0°C)")
	return value

def	test_temperature():
	inputs = ["25", "abc", "100", "-50"]
	for i in inputs:
		print(f"Input data is '{i}'")
		try:
			value = input_temperature(i)
			print(f"Temperature is now {value}°C\n")
		except ValueError as e:
			print(f"caugh input_temperature error: {e}\n")
	
	print("All tests completed — program didn't crash")

def	main():
	print("=== Garden Temperature Checker ===\n")
	test_temperature()

if __name__ == "__main__":
	main()
