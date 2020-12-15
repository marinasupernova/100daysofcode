import random


'''
def get_random():

    low_num = int(input("Please enter a low number: "))
    high_num = int(input("Please enter a high number: "))

    comp_num = random.randint(low_num, high_num)
    return comp_num
'''
'''Task 120

def add_numbs():
    num1 = random.randint(5,20)
    num2 = random.randint(5,20)
    user_answer = int(input("Please add two numbers " + str(num1) + " " + str(num2) + " :"))
    correct_answer = num1 + num2
    return {"user_answer": user_answer, "correct_answer": correct_answer }

def substract_num():
    num1 = random.randint(25,50)
    num2 = random.randint(1,25)
    user_answer = int(input("Please substract two numbers " + str(num1) + " " + str(num2) + " :"))
    correct_answer = num1 - num2
    return {"user_answer": user_answer, "correct_answer": correct_answer }


def compare(answer1, answer2): 
    if answer1 == answer2:
        print("Correct")
    else: 
        print("False, correct answer is", answer1)

print("1. Addition\n 2. Substraction\n ")
user_choice = int(input("Please choose 1 or 2 : "))

if user_choice == 1:
    answers = add_numbs()
    compare(answers["correct_answer"], answers["user_answer"])
else:
    answers = substract_num()
    compare(answers["correct_answer"], answers["user_answer"])
    
''' 





    



