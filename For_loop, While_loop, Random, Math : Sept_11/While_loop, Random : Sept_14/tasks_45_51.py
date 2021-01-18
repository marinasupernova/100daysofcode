'''Task 45 
total = 0
while total <= 50:
    num = int(input(" Enter a number: "))
    result = total + num
    print(f'Total is {result}')'''

'''Task 46
num = 0
while num <= 5:
    num = int(input("Enter a number:"))
print("The last number you entered was a:", num)'''

''''Task 47 my solution'

num_1 = int(input("Enter your first number: "))

total_1 = num_1 + num_2
num_3 = input("Do you want to enter another number: y/n ")
while num_3 == "y":
    num_3 = int(input("Enter this number: "))
    total_2 = total_1 + num_3
else:
    print(total_2)'''

"""Task 47 solution"""
'''num1 = int(input("Enter your first number: "))
total = num1
again = "y"
while again == "y":
    num2 = int(input("Enter another number: "))
    total = total + num2
    again = input(" Do you want to enter another number: y/n " )
print("The total is", total)'''


'''Task 48 
again = "y"
total = 0
while again == "y":
    name = input("Enter invitee's name: ")
    print(name, "has been invited")
    total = total + 1
    again = input("Do you want to invite somebody else? y/n  ")
print("The total of invitees is", total)'''

'''compnum = 50
num = 0
while compnum < 50:
    num = input("Guess the number: ")
    compnum = num + 1
    print(num, "is too low, please try again")
else:
    print(num, "is too high, please try again")'''


"""Programme 

compnum = 50
num = int(input("Enter a number"))
if num < 50:
    print(num, "is too low, please try again")
elif num > 50:
    print(num, "is too high, please try again")
elif num == 50:
    print("Well done")"""

'''Cycle'''

'''compnum = 50
count = 0
while count != compnum:
    guess = int(input("Enter a number: "))
    count = guess 
    print("Try again")
    if count == compnum:
        print("Well done! You made ", count, "attempts!")'''


   
"""compnum = 50
count = 1
guess = int(input("Enter a number: "))
while guess != compnum:
    if guess < compnum:
        print(guess, "is too low, please try again")
    elif guess > compnum:
        print(guess, "is too high, please try again")
    elif guess == compnum:
        count = count + 1
        print("Well done, you tool", count, "attempts")"""
    

"""Task 49 Solution:
compnum = 50
guess = int(input("Can you guess the number I am thinking of?  "))
count = 1
while guess != compnum:
    if guess < compnum:
        print("Too low")
    else: 
        print("Too high")
    count = count + 1
    guess = int(input("Have another guess:"))
print("Well done, you took", count, "attempts")"""


"""Task 50 My Solution
num = int(input(" Please enter a number between 10 and 20:"))
while num != 10 and num != 20:
    if num < 10: 
        print("Too low")
    elif num > 20:
        print("Too high")
    else: 
        print("Thank you")
    num = int(input("Try again:"))"""
    



'''num = int(input(" Please enter a number between 10 and 20:"))
while num < 10 or num > 20:
    if num < 10:
        print("Too low")
    else:
        print("Too high")
    num = int(input("Try again:"))
print("Thank you")'''






"""rhyme = print("There are green bottles hanging on the wall 
green bottles hanging on the wall and if 1 green bottle should accidently fall")

answer = bottle_num
if answer == 10:
bottle_num = int(input("How many bottles are hanging on the wall? "))"""

"""Task 51
bottle_number = 10
while bottle_number != -1
    num = int(input("How many bottles will be hanging on the wall? "))
    if num != bottle_number:
        print("Wrong answer")
    else:
        bottle_number = bottle_number - 1    
        print("There are", num, "green bottles hanging on the wall", num, "green bottles hanging on the wall, and if 1 green bottle should accidentally fall.")
"""






    
    



