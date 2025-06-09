from MyClasses import Music, Pet

myBand = Music("The Beatles", "John Lennon")

print(myBand.singer)

myPet = Pet("Fido", 5, "Dog") 
print(myPet.age)
print(myPet.name)
print(myPet.__dict__)