from abc import ABC, abstractmethod


class Swimmable(ABC):
    @abstractmethod
    def swim(self):
        pass


class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass


class Bird:
    def make_sound(self):
        return "Tweet!"


class Sparrow(Bird, Flyable):
    def fly(self):
        return "Воробей летит"


class Penguin(Bird, Swimmable):
    def swim(self):
        return "Пингвин плывет"


s = Sparrow()
p = Penguin()

for bird in [s, p]:
    print(bird.make_sound())
