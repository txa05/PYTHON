#!/usr/bin/env python3

class	Plant:
	def __init__(self, name, age, height):
		self._name = name
		self._height = height
		self._age = age
		self._plusAge = 1
		self._plusCm = 0.8
	def show(self):
		print(f"{self._name.capitalize()}: {round(self._height, 1)}cm, {self._age} days old")

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

	def get_name(self):
		return self._name

	def get_age(self):
		return self._age

	def get_heigh(self):
		return self._height

	def addAge(self, plusAge):
		self._plusAge = plusAge

	def addHeigh(self, plusCm):
		self._plusCm = plusCm

class Flower(Plant):
    def __init__(self, name, age, height, color):
        super().__init__(name, age, height)
        self._color = color
        self._bloomed = False

    def bloom(self):
        self._bloomed = True

    def show(self):
        super().show()
        print(" Color:", self._color)
        if self._bloomed:
            print("", self._name.capitalize(), " is blooming beautifully!")
        else:
            print("", self._name.capitalize(), "has not bloomed yet")

def main():
    print("=== Garden Plant Types ===\n===Flower")
    rose = Flower("rose", 10, 15.0, "red")
    rose.show()
    print("[asking the", rose.get_name(),"to bloom]")
    rose.bloom()
    rose.show()



if __name__ == "__main__":
    main()