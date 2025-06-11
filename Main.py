from MyClasses import Dog, Pet, Ultra
from Car import Car

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

pi = 3.14159

# Using f-string with formatting specifier
circle_area = f"The area of a circle with radius 4 is {pi * 4 ** 2:.2f} square units."
print(circle_area)  # Output: "The area of a circle with radius 4 is 50.27 square units."

for i in range(10):  # outer loop
    print("Outer loop iteration:", i)
    for j in range(5):  # inner loop
        print("Inner loop iteration:", j)