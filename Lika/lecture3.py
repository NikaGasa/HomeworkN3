# 1
class Cat:
    def eat(self):
        return "cat drinks milk"
    def walk(self):
        return "cat runs 10km/hr"
    def talk(self):
        return "cat says meow"

class Dog:
    def eat(self):
        return "dog eats meat"
    def walk(self):
        return "dog runs 15km/hr"
    def talk(self):
        return "dog says woof"

meow = Cat()
woof = Dog()
print(meow.eat())
print(woof.eat())
def catto(obj):
    return obj.eat(), obj.walk(), obj.talk()
print(catto(meow))
def doggo(obj):
    return obj.eat(), obj.walk(), obj.talk()
print(doggo(woof))

# 2
class Currency():
    def __init__(self, value, unit = 'GEL'):
        self.unit = unit
        self.value = value

    def __str__(self):
        return f"{self.value}.00 {self.unit}"

    def changeTo(self, currency = None):
        if self.unit =='GEL' and currency == 'USD':
            usd = self.value * 0.32
            return f"{self.value} {self.unit} is {usd} dollars"
        elif self.unit =='GEL' and currency == 'EUR':
            eur = self.value * 0.29
            return f"{self.value} {self.unit} is {eur} euros"
        elif self.unit =='GEL' and currency == 'RUB':
            rub = self.value * 26.7
            return f"{self.value} {self.unit} is {rub} rubles"
        elif self.unit == 'USD' and currency == 'GEL':
            gel = self.value * 3.1
            return f"{self.value} {self.unit} is {gel} laris"
        elif self.unit == 'USD' and currency == 'EUR':
            eur2 = self.value * 0.91
            return f"{self.value} {self.unit} is {eur2} euros"
        elif self.unit == 'USD' and currency == 'RUB':
            rub2 = self.value * 83
            return f"{self.value} {self.unit} is {rub2} rubles"


money = Currency(1000, 'GEL')
money2 = Currency(2000, 'USD')
print(money.changeTo('RUB'))
print(money2.changeTo('GEL'))
print(money + money2)
