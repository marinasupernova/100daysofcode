'''my_string = "python"


x = 0

for i in my_string:
    x = x + 1
    print(my_string[0:x])

for i in my_string:
    x = x - 1
    print(my_string[0:x])'''

#использовании переменной-счетчика «x», которая показывает количество символов, необходимых для вывода в этой итерации. В первом цикле for значение увеличивается, пока не доберется до значения количества символов в слове. Во втором — опускается до нуля, пока на экране не останется ни одного символа.

#цикл while
#Сначала программа оценивает условие цикла while. Если оно истинное, начинается цикл, и тело while исполняется. Тело будет исполняться до тех пор, пока условие остается истинным. Если оно становится ложным, программа выходит из цикла и прекращает исполнение тела.


'''a = 1

while a < 10:
    print("Цикл выполнился", a, "раз")
    a = a + 1
print("Цикл окончен")'''


'''a = 1

while a < 5:
    print("условие верно")
    a = a + 1
else:
    print("условие neверно")'''


'''i = 1 

while i < 6:
    print(i)
    i += 1'''

#Для цикла while необходимо, чтобы соответствующие переменные были объявлены, в этом примере нам нужно объявить переменную индексации i, которую мы установили в 1.
'''
for i in range(0, 100):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print("-")
'''


'''
for i in range (0, 8):
    age = int(input("How old are you? "))
    if age < 31:
        print("More")
    elif age > 31:
        print("Less")
    else:
        print("Correct")
break
'''
'''
import random

down = 0
up = 100

for i in range(1, 10):
    guessed_age = random.randint(1, 100)
    answer = input("Are you" + str(guessed_age) + "years old?")
    if answer == "correct":
        print("Nice")
        break
    elif answer == "less":
        up == guessed_age
    elif answer == "more":
        down = guessed_age
    else:
        print("wrong answer")

'''


'''text = "krlglaer,arelg,,,,,,,,,rgaergaergdgbdfbgzdrgtaertga......."

textlist = [*text]'''


'''coma = ","
period = "."

if coma in textlist:
    coma = period'''

'''coma = ","
period = "."
i = 0

for i in textlist:

    if textlist[0] == ",":
        coma = period
        i += 1

print(textlist)'''


'''
word = "abrakadabra"

count = 0

for x in word:  
    if x == "a":
        count = count + 1
print("A = ", count)
'''


'''    
text = "krlglaer,arelg,,,,,,,,,rgaergaergdgbdfbgzdrgtaertga......."
count = 0
for x in text:
    if x == ",":
        count = count + 1
print("Comas =", count )
'''