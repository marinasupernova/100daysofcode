'''print("Hello, person!")'''
'''def greet():
    print("Hello, person!")
greet()'''

'''def greet(name):
    print(f"Hello, {name}!")

greet("Marina")'''

'''def greet(name, is_new):
    if(is_new):
        print(f"Hello, {name}! Nice to meet you!")
    else:
        print(f"What’s up, {name}? Nice to see you again!")

greet("Tom", False)
greet("Eva", True)'''

'''def superpower(name, power):
    print(f"Hi, I'm Super {name} and my superpower is {power}!")

superpower("Marina", "knowledge")'''

'''Activity 2'''
'''def funny_greeting (color, dessert):
    print(f"My favorite dessert is {color} because it tastes so good, and my favorite color is {dessert} because it is very pretty!!")

funny_greeting("blue", "chocolate pie")'''

'''Activity 3:'''
'''from datetime import datetime
from datetime import timedelta

def world_times():
    my_city = datetime.now()
    berlin = my_city + timedelta(hours=0)
    baguio = my_city+ timedelta(hours=7)
    tokyo = my_city + timedelta(hours=7)
    all_times = 
    print(all_times)'''

'''world_times()'''

'''Activity 4
def factorial(number):
    result = 1
    while number >= 1:
        result = result * number
        number = number - 1
    return result

final_result = factorial(4)

print(final_result)'''


'''Activity 5
def dessert_sorter(desserts):
    for i in range(desserts): 
        if i % 3 == 0:
            print("cupcake")
        elif i % 5 == 0:
            print("cookie")
        elif i% 5 == 0 / 5 and i % 3 == 0:
            print("It's a cupcakecookie!")
final_result = dessert_sorter(15)

print(final_result)'''


'''Activity Rock, paper, scissors'''

'''print("Welcome to the Rock Paper Scissors Game!")

player_1 = "Marina"
player_2 = "Katya"

def compare(item_1, item_2):
    if item_1 == "rock" and item_2 == "paper":
        print("Paper wins!")
    elif item_1 == "rock" and item_2 == "scissors":
        print("Rock wins!")
    elif item_1 == "rock" and item_2 == "rock":
        print("It's a tie!")
    elif item_1 == "paper" and item_2 == "rock":
        print("Paper wins!")
    elif item_1 == "paper" and item_2 == "scissors":
        print("Scissors win!")
    elif item_1 == "paper" and item_2 == "paper":
        print("It's a tie!")
    elif item_1 == "scissors" and item_2 == "rock":
        print("Rock wins!")
    elif item_1 == "scissors" and item_2 == "paper":
        print("Scissors wins!")
    elif item_1 == "scissors" and item_2 == "scissors":
        print("It's a tie!")
    else:
        print("The choice is not possible. You have not entered rock, paper or scissors.")
    

player_1_choice = "paper"
player_2_choice = "well"
print(compare(player_1_choice, player_2_choice))

везде вместо print return почему
 в случае сравнения одинаковых предметов можно было сравнить item 1 == item 2

'''

'''Challenge 1 Hangman'''

import time
name = input("What is your name?")
print(f'Hello, {name}!')

time.sleep(1)
print("Start guessing... ")
time.sleep(0.5) 


secret_word = "coding"
guesses = ''

max_turns = 11

while max_turns > 0:
    incor_guesses = 0
    max_turns -= 1
    
    current_state = ""
    for char in secret_word:
        if char in guesses:
            current_state += char
        else: 
            current_state += "_"
            incor_guesses += 1  
    print(current_state) 

    guess = input("Guess a charachter: ")
    guesses += guess
    
    if guess not in secret_word:
        print("Wrong guess")
        print(f"You have {max_turns} more guesses remaining")
        if max_turns == 0:
            print("Unfortunately for you, {name}, you've lost!")


print("incor guesses:", incor_guesses)
if incor_guesses == 0:
    print("You won!")
