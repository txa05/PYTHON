#!/usr/bin/env python3

class	Plant:
	def __init__(self, name, age, height):
		self._name = name
		self._height = height
		self._age = age
		self._plusAge = 1
		self._plusCm = 0.8
		self.status = self.PlantStatus()
	def show(self):
		print(f"{self._name.capitalize()}: {round(self._height, 1)}cm, {self._age} days old")
		self.status.incrShowState()

	def grow(self):
			self._height += self._plusCm
			self.status.incrGrowState()
	def age(self):
			self._age += self._plusAge
			self.status.incrAgeState()
	
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
	
	@classmethod
	def create_plant(cls, name, age, height):
		return cls(name, age, height)
	
	@staticmethod
	def is_old(age):
		return age > 365
	
	class	PlantStatus:
		def	__init__(self):
			self._grow_calls = 0
			self._age_calls = 0
			self._show_calls = 0

		def	incrGrowState(self):
			self._grow_calls += 1

		def	incrShowState(self):
			self._show_calls += 1

		def	incrAgeState(self):
			self._age_calls += 1
		
		def	displayStatus(self):
			print(f"Stats: {self._grow_calls} grow, {self._age_calls} age, {self._show_calls} show")

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

class	seed(Flower):
	def __init__(self, name, age, height, color):
		super().__init__(name, age, height, color)
		self._bloomed = False
		self._seed = 0
	
	def	show(self):
		super().show()
		print(f" seeds: {self._seed}")

	def grow(self):
		super().grow()
		self._seed += 2

class	Tree(Plant):
	def __init__(self, name, age, height, trunk_diameter):
		super().__init__(name, age, height)
		self._trunk_diameter = trunk_diameter
		self.status = self.PlantStatus()
		
	class	PlantStatus(Plant.PlantStatus):
		def	__init__(self):
			super().__init__()
			self._produce_shade_calls = 0

		def displayStatus(self):
			super().displayStatus()
			print(f"{self._produce_shade_calls} shade")
			
	def produce_shade(self):
		print(f"Tree {self._name.capitalize()} now produces a shade of {round(self._height, 1)}cm long and {round(self._trunk_diameter, 1)}cm wide")
		self.status._produce_shade_calls += 1
		
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


def	main():
	print("=== Garden Analytics ===\n=== Check year-old")
	print("is 30 days old than a year? —>", Plant.is_old(30))
	print("is 400 days old than a year? —>", Plant.is_old(400))
	print("\n=== Flower")
	rose = Flower("rose", 10, 15.0, "red")
	rose.show()
	print("[statistics for rose]")
	rose.status.displayStatus()
	print("[asking the", rose.get_name(),"to grow and bloom]")
	rose.bloom()
	rose.grow()
	rose.show()
	print("[statistics for rose]")
	rose.status.displayStatus()

	print("\n=== Tree")
	oak = Tree("oak", 365, 200.0, 5.0)
	oak.show()
	print("[statistics for oak]")
	oak.status.displayStatus()
	print("[asking the oak to produce shade]")
	oak.produce_shade()
	print("[statistics for oak]")
	oak.status.displayStatus()

	print("\n=== Seed")
	sunflower = seed("sunflower", 45, 80.0, "yellow")
	sunflower.show()
	print(f"[make sunflower grow, age and blom]")
	sunflower.grow()
	sunflower.age()
	sunflower.bloom()
	sunflower.show()
	sunflower.status.displayStatus()

	print("\n=== Anonimous")
	unknown = Plant.create_plant("Unknown plant", 0, 0.0)
	unknown.show()
	print(f"[statistics for {unknown.get_name()}]")
	unknown.status.displayStatus()

if __name__ == "__main__":
    main()