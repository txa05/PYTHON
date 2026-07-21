#!/usr/bin/env python3

class	GardenError(Exception):
		def	__init__(self, msg: str = "Unknown plant error") -> None:
			super().__init__(msg)

class	PlantError(GardenError):
	pass

class	WaterError(GardenError):
	pass

def	testing_garden_errors(error_type: str) -> None:
	if (error_type == "WaterError"):
		raise	WaterError("Not enough water in tank!")
	elif (error_type == "PlantError"):
		raise	PlantError("The tomato plant is wilting!")
	elif (error_type == "garden"):
		raise	GardenError("This flower is already bloomed")
	
def	catching_myexceptions() -> None:
	error_case = ["PlantError", "WaterError"]
	for i in error_case:
		print(f"\nTesting {i}...")
		try:
			testing_garden_errors(i)
		except PlantError as error:
			print(f"caught {error.__class__.__name__}: {error}")
		except WaterError as error:
			print(f"caught {error.__class__.__name__}: {error}")

def	catching_withbases() -> None:
	print("Testing catching all garden errors...")

	for i in ["PlantError", "WaterError"]:
		try:
			testing_garden_errors(i)
		except GardenError as error:
			print(f"Caught {error.__class__.__name__}: {error}")

def	main():
	print("=== Custom Garden Errors Demo ===")
	catching_myexceptions()
	print("")
	catching_withbases()
	print("\nAll custom error types work correctly!")

if __name__ == "__main__":
	main()