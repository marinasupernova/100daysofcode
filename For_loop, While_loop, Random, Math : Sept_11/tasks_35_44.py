'''for i in range (1, 10):
    print(i)'''

'''for i in range(1,10,2):
        print(i)'''


'''for i in range(10, 1,-3):
    print(i)'''

'''word = "wolf"
for i in word:
    print(i)'''


'''Task 35 
name = input("Type your name:")
for i in range (0,3):
    print(name)'''

'''Task 36
name = input("Type your name:")
num = int(input("Type any number:"))
for i in range (0, num) :
    print(name)'''

'''Task 37
name = input("Enter your name:")
for i in name:
    print(i)'''

'''Task 38   откуда знает что range  это относится к name a не к num
name = input("Enter your name:")
num = int(input("Type any number:"))
for x in range (0, num):
    for i in name:
        print(i)''' 

'''Task 39
num = int(input("Type a number between 1 and 12:"))
for i in range(1,13):
    answer = i * num
    print(i, "x", num, "=", answer)'''

'''Task 40 
num = int(input("Type a number below 50:"))
for i in range (50, num-1, -1):
    print(i) почему и а не number''' 

'''Task 41 
name = input("Enter your name:")
num = int(input("Type any number:"))
if num < 10:
    for i in range (0, num):
        print(name)
else:
    message = "Too high"
    for x in range (0,3):
        print(message)'''

'''Task 42 total = 0
for i in range (0,5):
    num = int(input("Type a number: "))
    answer = input("Do you want that number included? (yes/no) ")
    if answer == "yes":
        total = total + num
print(total)'''


'''Task 43 
answer = input("Which direction do you want to count? up/down ")
if answer == "up":
    up_count = int(input("Enter a top number: "))
    for i in range (1, up_count+1):
        print(i)
elif answer == "down":
    down_count = int(input("Enter a number below 20: "))
    for i in range (20, down_count-1, -1):
        print(i)
else:
    print("I don't understand")'''

'''Task 44 не та последовательность (после иф введи имя а не наоборот)


num_people = int(input("How many people do you want to invite to the party? "))
if num_people < 10:
    for i in range (0, num_people):
        names[i] = input("Enter a name: ")
        print(f'{names[i]} has been invited.')
else:
    print("Too many people")'''