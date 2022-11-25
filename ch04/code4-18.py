# 디미터의 법칙 준수 (좋음)

class Person:
    def __init__(self, coffee_cup):
        self.coffee_cup = coffee_cup

    def price_per_cup(self):
        cups = 798
        return self.coffee_cup.get_cost_per_cup(cups)

        
class Coffee_Machine:
    def __init__(self, price):
        self.price = price

    def get_price(self):
        return self.price


class Coffee_Cup:
    def __init__(self, machine):
        self.machine = machine

    def get_creator_machine(self):
        return self.machine

    def get_cost_per_cup(self, cups):
        return self.machine.get_price() / cups


m = Coffee_Machine(399)
c = Coffee_Cup(m)
p = Person(c)

print('Price per cup:', p.price_per_cup())
# 0.5