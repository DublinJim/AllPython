"""A class representing a pet."""

from datetime import date
import os

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.current_year = date.today().year

    def howOld(self):
        print("aged", self.age)

    def yearBorn(self):
        print("Born in", self.current_year - self.age)


class Dog(Pet):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def saybreed(self):
        print(self.breed)


class Ultra:
    def __init__(self, Pet, Dog):
        self.Pet = Pet
        self.Dog = Dog
