'''simple_array = [[2,5,8],[3,7,4],[1,6,9]]
print(simple_array[1])

simple_array[2][1] = 5
print(simple_array)

simple_array[1][2] = 5
print(simple_array)

simple_array[1].append(3)
print(simple_array)

data_set = {"A": {"x": 54, "y": 82, "z": 91}, "B": {"x": 75, "y": 29, "z": 80}}
print(data_set["A"])
print(data_set["B"] ["y"])

data_set["B"]["y"] = 53
print(data_set["B"] ["y"])

for i in data_set:
    print(data_set [i]["y"])

grades[name] = {"Math": mscore, "English": escore} #add another row of data t a 2Ddictionary: name - row index, Math English - column indexes

for name in grades: 
    print((name), grades[name]["English"])

del list[getRid]

Task 096, 097

simple_list = [[2, 5, 8],[3, 7, 4], [1, 6, 9], [4, 2, 0]]

row = int(input("Please select a row from 0 till 3: "))
column = int(input("Please select a row from 0 till 2: "))
print(simple_list[row][column])


Task 098

simple_list = [[2, 5, 8],[3, 7, 4], [1, 6, 9], [4, 2, 0]]

row = int(input("Please select a row from 0 till 3: "))
print(simple_list[row])

new_value = int(input("Please enter a new value: "))

simple_list[row].append(new_value)

print(simple_list[row])

Task 099

simple_list = [[2, 5, 8],[3, 7, 4], [1, 6, 9], [4, 2, 0]]

row = int(input("Please select a row from 0 till 3: "))
print(simple_list[row])

col = int(input("Please select a column from this row from 0 to 2: "))
print(simple_list[row][col])

change = input("Do you want to change this value? y/n ")

if change == "y":
    new_value = int(input("Please enter a new value: "))
    simple_list[row][col] = new_value

print(simple_list[row])

Task 100

sales = { 
"John" : {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
"Tom" : {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
"Anne" : {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
"Fiona" : {"N": 3904, "S": 3645, "E": 8821, "W": 2451},}

name = input("Please enter a salesperson name: ")
region = input("Please enter a region: ")

print(sales[name][region])


name = input("Please enter a name you want to change: ")
region = input("Please enter a region you want to change: ")

print(sales[name][region])

fig_change = input("Please enter a figure you want to alter: ")

sales[name][region] = fig_change
print(sales[name])'''


'''Task 102'''

'''wrong solution new_list = {"Names": {}, "Age":, "Shoe_size": }

name = input("Please enter 4 people's names: ")
age = int(input("How old are they? ")
shoe_size = int(input("What is your shoe size? "))


new_list = {}

for i in range (0, 4):

    name = input("Please enter a name: ")
    age = int(input("How old are they? "))
    shoe_size = int(input("What is your shoe size? "))
    new_list[name] = {"Age":age, "Shoe size":shoe_size}

ask = input("Please enter a name from the above: ")

print(new_list[ask])


Task 103 = 104

new_list = {}

for i in range (0, 3):

    name = input("Please enter a name: ")
    age = int(input("How old are they? "))
    shoe_size = int(input("What is your shoe size? "))
    new_list[name] = {"Age":age, "Shoe size":shoe_size}

"""for name in new_list:
    print((name), new_list[name]["Age"])"""



getRid = input("Please enter a name you want to delete: ")

del new_list[getRid]

for name in new_list:
    print((name), new_list[name]["Age"], new_list[name]["Shoe size"])'''

'''s = 0; i = -5

while i < 4: 
    i = i + 1
    if i == 0: continue
    print(i)
    s += 1/i

print(s)


for x in range (5, 0, -1): # выводит от 5 до 1  
    print(x)


msg = "Hello World!"

for x in msg:
    print(x) # Здесь строка выступает как список'''



'''str3 = """ ergrsth
rthsrth
serthsrth"""  #многострочность 

print(str3)


msg = "Hello" + " " + "world!"
print(msg)

 

# Преобразование числа в строку для конкатенации
num = 5
word = "cat"
samen = word + str(num)
print(samen)


message_True = str(True)
print(message_True)


#размножить строку

word = "success"
msg = word*1000

#проверять содеожиться ли строка
s = "abcdefghigk"
"abc" in s

#строки можно сравнивать в лексикографическом порядке - те перебираюся сммволы строк и когда доходят до сиивола кот имеет большее число в соотвествии с кодовой таблицей

Code
Cat 
ord("t") # проверить код символа 
ord("d")

word = "abcdefgh"[1]
print(word)'''


#срезы 

msg = "Hello world!"
print(msg[6:11])

print(msg[:3])
print(msg[3:])
print(msg[:]) #вся строка











