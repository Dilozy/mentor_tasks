from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Car(Transport):
    def start_engine(self):
        print("Машина завелась")

    def stop_engine(self):
        print("Машина заглохла")

    def move(self):
        print("Машина поехала")


class Boat(Transport):
    def start_engine(self):
        print("Лодка завелась")

    def stop_engine(self):
        print("Лодка заглохла")

    def move(self):
        print("Лодка поплыла")
