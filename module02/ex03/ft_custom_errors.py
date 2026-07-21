#!/usr/bin/env python3

class	GardenError(Exception):
		def	__init__(self, msg: str = "Unknow plant error") -> None:
			super().__init__(msg)

class	PlantError(GardenError):
	pass

class	WaterError(GardenError):
	pass

def	testing_garden_errors(error_type: str) -> None:
	if (error_type == "water"):
		raise	WaterError("Not enough water in tank!")
	elif (error_type == "plant"):
		raise	PlantError("The tomato plant is wilting!")
	elif (error_type == "garden"):
		raise	GardenError("This flower is already bloomed")
	
def	catching_costuexceptions():
	error_case = ["plant", "garden", "water"]