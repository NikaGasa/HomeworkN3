class Fruit:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __add__(self, other):
        return self.weight + other.weight
    def __eq__(self, other):
        if self.name == other.name:
            return "These are the same fruit"
        else:
            return f"{self.name} and {other.name} are different fruit"

apple = Fruit('apple', 2.5)
peach = Fruit('peach', 1.9)
Apple = Fruit('apple', 3)
print(apple.__add__(peach))
print(apple.__eq__(peach))
print(Apple.__eq__(apple))