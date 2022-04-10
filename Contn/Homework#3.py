import sqlite3

connect = sqlite3.connect('census.db')
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS density
                (province_or_territory VARCHAR,
                population INTEGER,
                land_area FLOAT);''')

list1 = [
    ('Newfoundland and Labrador', 512930, 370501.69),
    ('Prince Edward island', 135294, 5684.39),
    ('Nova Scotia', 908007, 52917.43),
    ('Quebeck', 7237479, 1357743.08),
    ('Alberta', 2974807, 639987.12)
]

cursor.executemany("INSERT INTO density (province_or_territory, population, land_area) VALUES (?,?,?) ", list1)
connect.commit()
cursor.execute("SELECT * FROM density")
# 4
m = cursor.fetchmany(5)
for row in m:
    print(row)
# 5
cursor.execute('SELECT population FROM density')
p = cursor.fetchmany(5)
for each in p:
    print(each)
# 6
cursor.execute('SELECT province_or_territory,population FROM density WHERE population > 1000000')
pop = cursor.fetchmany(2)
for popu in pop:
    print(popu)
# 7-8
cursor.execute('SELECT province_or_territory, population FROM density WHERE population<1000000 OR population>5000000')
mil = cursor.fetchmany(4)
for each in mil:
    print(each)
# 9
cursor.execute('SELECT province_or_territory, land_area FROM density WHERE land_area > 200000')
area = cursor.fetchmany(3)
for each in area:
    print(each)
