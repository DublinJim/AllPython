from MyClasses import Dog, Pet, Ultra

myPet = Pet("Fido", 5)

print(myPet.__dict__)
print("This is myPet Object ID: " + str(id(myPet)))
myPet.howOld()
myPet.yearBorn()
myDog = Dog("Fido", 5, "Golden Retriever")
myDog.saybreed()

myUltra = Ultra(myPet, myDog)

myUltra.Pet.howOld()
myUltra.Dog.saybreed()
