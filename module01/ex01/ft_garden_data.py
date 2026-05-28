#!/usr/bin/env python3

class	Plant:
	def __init__(self, name, heigh, age):
		self.name = name
		self.heigh = heigh
		self.age = age
	
	def show(self):
		print(f"{self.name}: {self.heigh}cm, {self.age} days old")

def	main():
	print("=== Garden Plant Registry ===")
	r = Plant("Rose", 25, 30)
	s = Plant("Sunflower", 80, 45)
	c = Plant("Cactus", 15, 120)
	r.show()
	s.show()
	c.show()

if __name__ == "__main__":
	main()