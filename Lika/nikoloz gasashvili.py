# 1
try:
    age = int(input("ჩაწერეთ თქვენი ასაკი: "))
    if 0 <= age <= 10:
        print("ბავშვი")
    elif 11 <= age <= 19:
        print("თინეიჯერი")
    elif 20 <= age <= 30:
        print("ახალგაზრდა")
    elif 31 <= age <= 50:
        print("ზრდასრული")
    elif 51 <= age <= 80:
        print("ასაკოვანი")
    elif 81 <= age <= 100:
        print("მხცოვანი")
    else:
        print("დენიკინის დროინდელი")
except:
    print("ასაკი ჩაწერეთ მთელ რიცხვებში")

# 2
def secondassignment(number):
    sum = 0
    numb = int(number)
    for i in range(1, numb):
        if numb % i == 0:
            sum += i
        if numb == sum:
            return numb

FILE = open('perfect number assignment', 'w')
inpu = int(input("ჩაწერეთ რიცხვი: "))
for i in range(1,inpu):
    if secondassignment(i):
        FILE.write(i + "\n")


# 3
list = ['Nika',"Gio","Daviti", "Elizabeti","Joni"]
list2 = []
def fun(list):
    s = sorted(list)
    print(s)

fun(list)
