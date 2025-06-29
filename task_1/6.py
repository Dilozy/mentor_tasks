from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Flyable:
    def fly(self):
        return "I'm flying!"


class Swimmable:
    def swim(self):
        return "I'm swimming!"


class Dog(Animal):
    def speak(self):
        return "Woof!"
    
    def move(self):
        return "I'm running!"
    

class Bird(Animal, Flyable):
    def speak(self):
        return "Tweet!"
    
    def move(self):
        return self.fly()
    

class Fish(Animal, Swimmable):
    def speak(self):
        return "..."
    
    def move(self):
        return self.swim()


animals = [Dog(), Bird(), Fish()]
for animal in animals:
    print(f"{animal.__class__.__name__}: {animal.speak()}, {animal.move()}")
