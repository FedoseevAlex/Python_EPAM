import abc

class Vehicle(abc.ABC):
    """
    Abstract class for any vehicle
    """
    wheels_number = None
    def __init__(self, trademark: str, model: str, mileage: int, initial_price):
        self.trademark = trademark
        self.model = model
        self.mileage = mileage
        self.initial_price = initial_price

    @classmethod
    def is_motorcycle(cls):
        return cls.wheels_number == 2

    @abc.abstractmethod
    def vehicle_type(self) -> str:
        """
        Returns a vehicle name
        :return: vehicle name as a str
        """

    def purchase_price(self):
        return self.initial_price - 0.1 * self.mileage


class Car(Vehicle):
    wheels_number = 4

    def vehicle_type(self):
        return ' '.join(['Car', self.trademark, self.model])

class Motorcycle(Vehicle):
    wheels_number = 2

    def vehicle_type(self):
        return ' '.join(['Motorcycle', self.trademark, self.model])

class Truck(Vehicle):
    wheels_number = 6

    def vehicle_type(self):
        return ' '.join(['Truck', self.trademark, self.model])

class Bus(Vehicle):
    wheels_number = 4

    def vehicle_type(self):
        return ' '.join(['Bus', self.trademark, self.model])

m = Motorcycle('Yamaha', 'MT-09', 1000, 13_000)
c = Car('Opel', 'Astra', 500, 10_000)
t = Truck('KAMAZ', '4911', 70_000, 100_000)
b = Bus('MAZ', '903065', 1000, 120_000)