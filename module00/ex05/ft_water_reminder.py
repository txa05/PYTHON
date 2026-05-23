def ft_water_reminder():
	a = int(input("Days since last watering: "))
	plant_status = "Plants are fine" if a <= 2 else "Water the plants!"
	print(plant_status)