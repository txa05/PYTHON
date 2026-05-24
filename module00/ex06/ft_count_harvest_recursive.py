def	recursive_print(value):
	if (value < 1):
		return
	recursive_print(value - 1)
	print("Day", value)

def	ft_count_harvest_recursive():
	days = int(input("Days until harvest: "))
	recursive_print(days)
	print("Harvest time!")