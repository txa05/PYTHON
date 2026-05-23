def ft_plant_age():
	a = int(input("Enter plant age in days: "))
	status = "Plant is ready to harvest!" if a > 60 else "Plant needs more time to grow."
	print(status)