from abc import ABC, abstractmethod


class Runnable(ABC):
    @abstractmethod
    def run(self):
        pass


class Swimmable(ABC):
    @abstractmethod
    def swim(self):
        pass


class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass


class Lion(Runnable):
    def run(self):
        return "Лев бежит"
