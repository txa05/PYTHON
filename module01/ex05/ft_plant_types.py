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

class Tree(Plant):
    def __init__(self, name, age, height, trunk_diameter):
        super().__init__(name, age, height)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"Tree {self._name.capitalize()} now produces a shade of {round(self._height, 1)}cm long and {round(self._trunk_diameter, 1)}cm wide")
    
    def show(self):
        super().show()
        print(f"Trunk diameter: {round(self._trunk_diameter, 1)}cm")

class Vegetable(Plant):
    def __init__(self, name, age, height, harvest_season, nutri_value):
        super().__init__(name, age, height)
        self._nutri_value = nutri_value
        self._harvest_season = harvest_season 

    def show(self):
        super().show()
        print(f"Harvest season: {self._harvest_season}\nNutritional value: {self._nutri_value}")
    
    def grow(self):
        super().grow()
        self._nutri_value += 1


def main():
    print("=== Garden Plant Types ===\n=== Flower")
    rose = Flower("rose", 10, 15.0, "red")
    rose.show()
    print("[asking the", rose.get_name(),"to bloom]")
    rose.bloom()
    rose.show()

    print("\n=== Tree")
    oak = Tree("oak", 365, 200.0, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato = Vegetable("tomato", 10, 5.0, "April", 0)
    tomato.addHeigh(2.1)
    tomato.show()
    print(f"[make {tomato.get_name()} grow and age for 20 days]")
    for i in range(20):
        tomato.age()
        tomato.grow()
    tomato.show()
if __name__ == "__main__":
    main()