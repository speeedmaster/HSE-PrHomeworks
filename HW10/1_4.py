# Импользовал шаблон Flyweight 

from typing import Dict, Optional
import hashlib


class FlyweightCar:
    def __init__(self, brand: str, model: str, color: str):
        self.brand = brand
        self.model = model
        self.color = color

    def to_string(self):
        return '_'.join((self.brand, self.model, self.color))


class LightweightCarFactory:
    def __init__(self):
        self._hash_to_car: Dict[str, FlyweightCar] = dict()
        self._plate_to_hash: Dict[str, str] = dict()

    def add_car(self, car: FlyweightCar, plate: str) -> None:
        hash = hashlib.sha256(car.to_string().encode())
        if hash not in self._hash_to_car:
            self._hash_to_car[hash] = car
        self._plate_to_hash[plate] = hash
        

    def get_car(self, plate: str) -> Optional[FlyweightCar]:
        if plate not in self._plate_to_hash:
            return None
        return self._hash_to_car[self._plate_to_hash[plate]]


if __name__ == "__main__":
    factory = LightweightCarFactory()

    factory.add_car(FlyweightCar("Chevrolet", "Camaro2018", "pink"), "0001")
    factory.add_car(FlyweightCar("Mercedes Benz", "C300", "black"), "0002")
    factory.add_car(FlyweightCar("Mercedes Benz", "C500", "red"), "0003")
    factory.add_car(FlyweightCar("BMW", "M5", "red"), "0004")
    factory.add_car(FlyweightCar("BMW", "X6", "white"), "0005")
    factory.add_car(FlyweightCar("BMW", "M5", "red"), "0006")
    factory.add_car(FlyweightCar("BMW", "X1", "red"), "0007")