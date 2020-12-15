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
Task 121 
 
def add_name():
    name = input("Enter one name: ")
    lst.append(name)

def change_name():
    index = int(input("please enter an index of the name: "))
    name = input("Change the name: ")
    lst[index] = name

def del_name():
    name = input("Please enter a name you want to delete: ")
    lst.remove(name)

def view_names():
    for i in lst:
        print(i)

lst = []
exit = False

while exit != True:
    user_choice = int(input("Please select from the options below: \n 1.Add one name \n 2. Change the name \n 3. Delete the name \n 4. View the names \n 5. Exit \n")) 

    if user_choice == 1:
        add_name()
    elif user_choice == 2:
        change_name()
    elif user_choice == 3: 
        del_name()
    elif user_choice == 4: 
        view_names()
    elif user_choice == 5:
        exit = True
    else: 
        print("Wrong choice, select a number from the above")












    



