class Human:
    def __init__(self, name):
        self.name = name

class Bus:
    def __init__(self, model):
        self.model = model
        self.passengers = []

    def add_passenger(self, human):
        self.passengers.append(human)

    def info(self):
        print(f"Bus {self.model}")
        if self.passengers:
            print("Зараз в бусіку їдуть:")
            for h in self.passengers:
                print(h.name)
        else:
            print("Бусік порожній")
        print()

    def remove_passenger(self, name):
        for h in self.passengers:
            if h.name == name:
                self.passengers.remove(h)

bus = Bus("Ikarus 256")
bus.info()

h1 = Human("Ілюшка")
h2 = Human("Михаська")
h3 = Human("Маргоша")

bus.add_passenger(h1)
bus.add_passenger(h2)
bus.add_passenger(h3)
bus.info()

bus.remove_passenger("Михаська")
bus.info()