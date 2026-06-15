#!/usr/bin/env python3

class	Plant:
	def __init__(self, name, heigh, age, plusAge, plusCm):
		self.name = name
		self.heigh = heigh
		self.age = age
		self.plusAge = plusAge
		self.plusCm = plusCm
	def show(self):
		print(f"{self.name}: {self.heigh}cm, {self.age} days old")

	def grow(self, time):
		for i in range(time):
			print(f"=== Day {i + 1} ===")
			self.age += self.plusAge
			self.heigh += self.plusCm
			print(f"{self.name}: {self.heigh:.1f}cm, {self.age} days old")

def	main():
	rose = Plant("Rose", 25.0, 30, 1, 0.8)
	print("=== Garden Plant Growth ===")
	rose.show()
	days = 7
	rose.grow(days)
	print(f"Growth this week: {rose.plusCm * days:.1f}cm")
	

if __name__ == "__main__":
	main()