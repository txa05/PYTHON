#!/usr/bin/env	python3

plants = []

class	GardenError(Exception):
		def	__init__(self, msg: str = "Unknown plant error") -> None:
			super().__init__(msg)

class	PlantError(GardenError):
	pass

class	WaterError(GardenError):
	pass

def	water_plant(plant_name) -> None:
	if plant_name != plant_name.capitalize():
		raise PlantError(f"Invalid plant name to water: '{plant_name}'")
	print(f"Watering {plant_name}: [OK]")

def	test_watering_system() -> None:
	print("Opening watering system")
	try:
		for plant in plants:
			water_plant(plant)
	except PlantError as err:
		print(f"Caught {err.__class__.__name__}: {err}")
		print(".. ending tests and returning to main")
	finally:
		print("Closing water system")


def	main():
	print("=== Garden Watering System ===\n")

	print("Testing valid plants")
	global plants
	plants = ["Tomato", "Lettuce", "Carrots"]
	test_watering_system()
	
	print("\nTesting invalid plants")
	plants = ["Tomato", "lettuce"]
	test_watering_system()

	print("\nCleanup always happens, even with errors!")

if __name__ == "__main__":
	main()