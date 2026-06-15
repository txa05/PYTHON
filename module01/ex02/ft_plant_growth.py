#!/usr/bin/env python3

class	Plant:
	def __init__(self, name, heigh, age):
		self.name = name
		self.heigh = heigh
		self.age = age
	def show(self):
		print(f"{self.name}: {self.heigh}cm, {self.age} days old")

	def grow(self):
		print(f"{self.name}: {self.heigh + 0.8}cm, {self.age + 1} days old")

def	main():
	