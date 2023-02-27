class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]


ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('focus')

for car in ford:
    print(car)
