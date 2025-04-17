class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} is moving.")

class Dog(Animal):
    def move(self):
        print(f"{self.name} is running.")

class Bird(Animal):
    def move(self):
        print(f"{self.name} is flying.")

class Fish(Animal):
    def move(self):
        print(f"{self.name} is swimming.")

class Vehicle:
    def __init__(self, model):
        self.model = model

    def move(self):
        print(f"The {self.model} is moving.")

class Car(Vehicle):
    def move(self):
        print(f"The {self.model} is driving. 🚗")

class Plane(Vehicle):
    def move(self):
        print(f"The {self.model} is flying. ✈️")

class Boat(Vehicle):
    def move(self):
        print(f"The {self.model} is sailing. 🛥️")

# Demonstrate polymorphism
animals = [Dog("Buddy"), Bird("Tweety"), Fish("Nemo")]
vehicles = [Car("Sedan"), Plane("Boeing 747"), Boat("Sailboat")]

print("Animals moving:")
for animal in animals:
    animal.move()
    print("-" * 20)

print("\nVehicles moving:")
for vehicle in vehicles:
    vehicle.move()
    print("-" * 20)

# Another way to demonstrate polymorphism with a function
def make_it_move(thing):
    thing.move()

print("\nMaking things move through a function:")
dog = Dog("Max")
car = Car("SUV")
make_it_move(dog)
make_it_move(car)
