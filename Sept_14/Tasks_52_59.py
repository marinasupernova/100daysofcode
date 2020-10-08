import random
'''import random
num = random.random()

print(num)'''

'''import random
color = random.choice (["red", "black", "greeen"])
print(color)'''

'''Task 52
num = random.randint(1,100)
print(num)'''

'''Task 53
fruits = random.choice(["apple", "banana", "apricot", "cherry", "peach"])
print(fruits)'''

'''Task 54
heads_or_tails = random.choice(["h", "t"])
user_choice = input("Please choose head or tails: h/t")
if user_choice == heads_or_tails:
    print("You won!")
else:
    print("Bad luck!")
print("The computer selected:", heads_or_tails)
if heads_or_tails =="h":
    print("It was heads")
else:
    print("It was tails")'''

'''Task 55
num = random.randint(1, 5)
guess_1 = int(input("Please pick a number:"))
if guess_1 == num:
    print("Well done!")
elif guess_1 < num:
    print("Too low")
    guess_1 = int(input("Try again:"))
    if guess_1 == num:
        print("Correct")
elif guess_1 > num:
    print("Too high")
    guess_1 = int(input("Try again:"))
    if guess_1 == num:
        print("Correct")
    else:
        print("You lose!")'''

"""Task 56
random_num = random.randint(1,10)
guess = 0
while guess != random_num:
    guess = int(input("Guess a number between 1 and 10: "))
print("You are right")"""


'''Task 57
random_num = random.randint(1,10)
guess = 0
while guess != random_num:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < random_num:
        print("Too low")
    elif guess > random_num:
        print("Too high")
print("You are right")'''


"""num = random.random()
num1 = num * 100
num2 = random.randint
print(num1)"""


"""num1 = random.randint(1,10)
num2 = random.randint(1,10)
q1 = int(input("How much is it:", num1 * num2))
q2 = int(input("How much is it:", num1 / num2))
q3 = int(input("How much is it:", num1 + num2))
q4 = int(input("How much is it:", num1 - num2))
q5 = int(input("How much is it:", (num1 - num2) * 3))"""

'''Task 58
score = 0

for i in range (1, 6):
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    answer = num1 + num2
    print("How much is:", num1, "+", num2, "?")
    guess = int(print("Your answer is: ")
    if guess == answer:
        score = score +1
print("Your total score is: ", score, "out of 5")'''


i = 0
for i in range (0, 6):
    color = random.choice(["red", "green", "blue", "violet", "white"])
    guess = input("Guess a color: ")
    if 
    print()
if guess == color:
    print("Well done")



