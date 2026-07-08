#!/usr/bin/env python3

class	Plant:
	def __init__(self, name, age, height):
		self.name = name
		self.heigh = height
		self._age = age
		self.plusAge = 1
		self.plusCm = 0.0
	def show(self):
		print(f"{self.name}: {round(self.heigh, 1)}cm, {self._age} days old")

	def grow(self):
			self.heigh += self.plusCm
	def age(self):
			self._age += self.plusAge
	def setAge(self, age):
		self._age = age
	def setHeigh(self, heigh):
		self.heigh = heigh
	def addAge(self, plusAge):
		self.plusAge = plusAge
	def addHeigh(self, plusCm):
		self.plusCm = plusCm

def	main():
	rose = Plant("Rose", 30, 1)
	rose.setHeigh(25.0)
	rose.addHeigh(0.8)
	rose.setAge(30)
	rose.addAge(1)
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