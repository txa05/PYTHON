#!/usr/bin/env python3

def	input_temperature(temp_str):
	value = int(temp_str)
	return value

def	test_temperature():
	print("input data is '25'")
	value = input_temperature("25")
	print(f"Temperature is now {value}°C")

	print("\nInput data is 'abc'")
	value = input_temperature("abc")
	print(f"temperature is now {value}°C")

def	main():
	try:
		print("=== Garden Temperature ===\n")
		test_temperature()
	except ValueError:
		print("Não podemos converter para número")
	except:
		print("Há algum erro no valor da temperatura actual\n")
	finally:
		print("\nAll tests completed — program didn't crash")

if	__name__ == "__main__":
	main()