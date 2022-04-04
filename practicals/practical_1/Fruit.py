class Fruit:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __add__(self, __o):
        if not isinstance(__o, Fruit):
            raise TypeError("can only add fruit")
        if self.name != __o.name:
            raise ValueError("can only add identical fruits")
        return Fruit(self.name, self.weight + __o.weight)

    def __eq__(self, __o):
        if not isinstance(__o, Fruit):
            return False
        return self.name == __o.name


apple = Fruit("Apple", 13)
orange = Fruit("Orange", 5)

print((apple + Fruit("Apple", 5)).weight)
print(apple == orange)
print(orange == orange)
# print(orange + apple)
# print(orange + 5)
