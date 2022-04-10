# 1
class People():
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_mail(self):
        pass
class Student(People):
    def __init__(self, firstname, lastname, courses):
        super().__init__(firstname, lastname)
        self.course = courses

    def get_mail(self):
        return f"{self.firstname}.{self.lastname}.1@btu.edu.ge"

class Lecturer(People):
    def __init__(self,firstname, lastname, salary):
        super().__init__(firstname, lastname)
        self.salary = salary

    def get_mail(self):
        return f"{self.firstname}.{self.lastname}.@btu.edu.ge"

# 2
class Libraryitems():
    def __init__(self, title, subject, status):
        self.title = title
        self.subject = subject
        self.status = status

    def booking(self):
        return f"You have booked book {self.title} in subject {self.subject}. duration of your booking is {self.status} days"

class Book(Libraryitems):
    def __init__(self, ISBN, authors, title, subject, status):
        super().__init__(title, subject, status)
        self.isbn = ISBN
        self.authors = authors
    def booking(self):
        return f"You have booked {self.authors}'s book {self.title} in subject {self.subject}. duration of your booking is {self.status} days"

class Magazine(Libraryitems):
    def __init__(self, journalname, volume, status):
        self.status = status
        self.jounalname = journalname
        self.volume = volume

    def booking(self):
        return

class CD(Libraryitems):
    def __init__(self, title = None, status = None):
        self.title = title
        self.status = status

    def __str__(self):
        return f"Our library doesnt have function to book CDs"


s = CD()
print(s)

# 3
class Contacts():
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class Mailsender():
    def send_mail(self):
        return f"თქვენი მეილი გაიგზავნა ამ მისამართზე: giorgi.giorgadze@gmail.com"

class Family(Contacts, Mailsender):
    def __init__(self, name, phone, email):
        super().__init__(name, phone)
        self.email = email

    def send_mail(self):
        return

class Friends(Contacts, Mailsender):
    def __init__(self, name, phone, email, birthdate):
        super().__init__(name, phone)
        self.email = email
        self.birthdate = birthdate

    def send_mail(self):
        return