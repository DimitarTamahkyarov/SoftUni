from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: int):
        ...

    @abstractmethod
    def refuel(self, fuel: int):
        ...


class Car(Vehicle):
    def drive(self, distance: int):
        consumption = (self.fuel_consumption + 0.9) * distance

        if consumption <= self.fuel_quantity:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel


class Truck(Vehicle):

    def drive(self, distance: int):
        consumption = (self.fuel_consumption + 1.6) * distance

        if consumption <= self.fuel_quantity:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel * 0.95


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)


