from car import carclass


class ElectroCar(carclass.CarClass):
    def __init__(self, brand, model, year, probeg):
        super().__init__(brand, model, year, probeg)
        self.battary = 100

    def description_battary(self):
        print(f"Этот автомобиль имеет мощность {self.battary}%")


if __name__ == '__main__':
    e_car = ElectroCar("Tesla1", "T1", 2018, 100000)
    e_car.show_car()
    e_car.description_battary()
