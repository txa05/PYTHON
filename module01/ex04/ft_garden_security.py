#!/usr/bin/env python3

class	Plant:
	def __init__(self, name, age, height):
		self.name = name
		self.heigh = height
		self._age = age
		self.plusAge = 1
		self.plusCm = 0.8
	def show(self):
		print(f"{self.name}: {round(self.heigh, 1)}cm, {self._age} days old")

	def grow(self):
			self.heigh += self.plusCm
	def age(self):
			self._age += self.plusAge
	def set_age(self, age):
		self._age = age
	def set_heigh(self, heigh):
		self.heigh = heigh
	def get_age(self):
		return self._age
	def get_heigh(self):
		return self.heigh
	def addAge(self, plusAge):
		self.plusAge = plusAge
	def addHeigh(self, plusCm):
		self.plusCm = plusCm

def	main():
	print("=== Print Factory Output ===")
	rose = Plant("Rose", 30, 25.0)
	oak = Plant("Oak", 365, 200.0)
	cactos = Plant("Cactos", 90, 5.0)
	sunflower = Plant("Sunflower", 45, 80.0)
	fern = Plant("Fern", 120, 15.0)

	Plantas = [rose, oak, cactos, sunflower, fern]

	for plant in Plantas:
		print("Created:", end=' ')
		plant.show()
if __name__ == "__main__":
	main()