class	Plant:
	def __init__(self, name, age, height):
		self._name = name
		self._height = height
		self._age = age
		self._plusAge = 1
		self._plusCm = 0.8
	def show(self):
		print(f"{self._name.capitalize()}: {round(self._height, 1)}cm, {self._age} days old")
		self.PlantStatus.incrShowState()

	def grow(self):
			self._height += self._plusCm
			self.PlantStatus.incrGrowState()
	def age(self):
			self._age += self._plusAge
			self.PlantStatus.incrAgeState()
	
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
	def is_old(obj):
		return obj._age > 365
	
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
