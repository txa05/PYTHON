#!/usr/bin/env python3

class	Plant:
	def __init__(self, name, age, height):
		self._name = name
		self._height = height
		self._age = age
		self._plusAge = 1
		self._plusCm = 0.8
	def show(self):
		print(f"{self._name}: {round(self._height, 1)}cm, {self._age} days old")

	def grow(self):
			self._height += self._plusCm
	def age(self):
			self._age += self._plusAge
	
	def set_age(self, age):
		if (age < 0):
			print(f"{self._name}: Error, age can't be negative\nAge update rejected")
			return
		self._age = age

	def set_heigh(self, height):
		if (height < 0):
			print(f"{self._name}: Error, height can't be negative\nHeight  update rejected")
			return
		self._height = height
	def get_age(self):
		return self._age
	def get_heigh(self):
		return self._height
	def addAge(self, plusAge):
		self._plusAge = plusAge
	def addHeigh(self, plusCm):
		self._plusCm = plusCm

def	main():
	print("=== Print Factory Output ===")
	rose = Plant("Rose", 10, 15.0)
	
	print(f"Plant created:", end=' ')
	rose.show()

	rose.set_age(30)
	rose.set_heigh(25.0)

	print("")

	print(f"Height updated: {rose.get_heigh()}cm")
	print(f"Age updated: {rose.get_age()} days")

	print("")
	rose.set_age(-2)
	rose.set_heigh(-4)

	print("Current state:", end=' ')
	rose.show()

if __name__ == "__main__":
	main()