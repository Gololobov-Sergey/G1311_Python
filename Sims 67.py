import random


class Human:
    def __init__(self, name, car=None):
        self.name = name
        self.car = car
        self.house = House()
        self.money = 100

    def work(self):
        pass

    def shopping(self):
        self.money -= random.randint(5, 10)
        self.house.food += random.randint(1, 10)
        if self.car == None:
            print("Пішли на шопінг пішки")
        else:
            if self.car.drive(random.randint(10, 20)):
                print("Поїхали на шопінг на авто")
            else:
                print("Немає бензину, пішли пішки")

    def eat(self):
        pass

    def chill(self):
        pass

    def cleaning(self):
        pass

    def info(self):
        pass

    def is_alive(self):
        return self.money > 0

    def live(self, day):
        pass


class Car:
    def __init__(self, model):
        self.model = model
        self.fuel = 60
        self.state = 100

    def drive(self, length):
        delta_fuel = length * 0.1
        if self.fuel - delta_fuel > 0:
            print(f"Ми проїхали {length} км, виратили {delta_fuel} л пального")
            self.fuel -= delta_fuel
            self.state -= length * 0.01
            return True
        else:
            print("Подорож неможлива, не вистачає пального")
            return False

    def add_fuel(self):
        pass

    def __str__(self):
        return f"Авто: {self.model}, пальне: {self.fuel} л, стан {self.state} %"


class House:
    def __init(self):
        self.food = 0
        self.pollution = 0

    def __str__(self):
        pass
