class Kettle(object):

    power_source = "electricity"

    # constructor
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    # self is like this from java refers to instance variables
    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.price)

# kenwood.switch_on()
Kettle.switch_on(kenwood)

print("switching to atomic power source")
Kettle.power_source = "atomic"

print("kenwood switched to gas")
kenwood.power_source = "gas"

print("Models: {0.make} = {0.price} {0.on}".format(kenwood))
print(Kettle.power_source)
print(kenwood.power_source)


print(Kettle.__dict__)
print(kenwood.__dict__)