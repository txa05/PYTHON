#!/usr/bin/env python3

class	Plant:
	def __init__(self, name, age, plusAge, heigh, plusCm):
		self.name = name
		self.heigh = heigh
		self._age = age
		self.plusAge = plusAge
		self.plusCm = plusCm
	def show(self):
		print(f"{self.name}: {round(self.heigh, 1)}cm, {self._age} days old")

	def grow(self):
			self.heigh += self.plusCm
	def age(self):
			self._age += self.plusAge

def	main():
	rose = Plant("Rose", 30, 1, 25.0, 0.8)
	print("=== Garden Plant Growth ===")
	rose.show()
	for i in range(7):
		print(f"=== Day {i + 1} ===")
		rose.age()
		rose.grow()
		rose.show()
	print(f"Growth this week: {round((i + 1) * rose.plusCm, 1)}cm")

if __name__ == "__main__":
	main()