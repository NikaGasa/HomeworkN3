# 1
class Book:
    def __init__(self, name, author, ryear, pages):
        self.name = name
        self.author = author
        self.ryear = ryear
        self.pages = pages

    def info(self):
        return f"this is {self.name}, its {self.author}'s book, was released ni {self.year}, pages:{self.pages}"

#2
class list:
    def __init__(self, list = []):
        self.list = list
    def min(self):
        return min(list)
    def max(self):
        return max(list)

m = list([2,5,8,7,3])
print(m.min())
