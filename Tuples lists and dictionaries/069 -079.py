'''fruit_tuple = ("apple", "banana", "strawberry", "orange")
print(fruit_tuple.index("strawberry"))
print(fruit_tuple[2])'''


names_list = ["John", "Tim", "Sam"]
'''del names_list[1]

names_list.append(input("Add a name: "))

names_list.sort() ### Sort and save ###

print(sorted(names_list)) ### Sort but not save ### '''

'''###
lists []
tuples ()
dictionaries{}  - content can be changed, indexes can not
### '''

'''colours = {1:"red", 2:"blue", 3:"green"}
colours[2] = "yellow"
print(colours)'''

x = [154, 634, 892, 345, 341, 43]
'''print(len(x))'''

'''print(x[1:4])'''

'''for i in x:
    print(i) - #to print an item on a list on a separate line'''


'''num = int(input("Enter number: "))
if num in x:
    print(num, "is in the list")
else:
    print("Not in the list")'''


'''x.insert(2, 420)
print(x)'''

'''x.remove(892)
print(x)'''

'''x.append(993)
print(x)'''

'''Task 69

countries = ("France", "Spain", "Norway", "Australia", "Namibia")
print(countries)
new_country = input("Add a country name from the list: ")
print(countries.index(new_country))'''

'''Task 70
countries = ("France", "Spain", "Norway", "Australia", "Namibia")
print(countries)
country = input("Please enter one of the countries from above: ")
print(country, "has index number", countries.index(country))
num = int(input("Enter a number form 0 to 4: "))
print(countries[num])'''


'''Task 71

sports = ["tennis","polo"]
sports.append(input("What is your favourite sport? "))
sports.sort()
print(sports)'''

'''Task 72

school_subjects = ["Math", "PE", "Sciences", "Art", "Economics", "Geography"]
print(school_subjects)
not_fav = input("Which of the subjects don't you like from the above ? ")
getrid = school_subjects.index(not_fav)
del school_subjects[getrid]
print(school_subjects)'''


'''Task 73
food_dictionary = {}
food1 = input("Enter your favorite food: ")
food_dictionary[1] = food1
food2 = input("Enter your favorite food: ")
food_dictionary[2] = food2
food3 = input("Enter your favorite food: ")
food_dictionary[3] = food3
food4 = input("Enter your favorite food: ")
food_dictionary[4] = food4
print(food_dictionary)
notfav = int(input("Which one do you want to remove? "))
del food_dictionary[notfav]
print(sorted(food_dictionary.values()))'''



'''Task 74

colors_list = ["red", "green", "blue", "pink", "yellow", "white", "black", "white", "violet", "indigo"]
strt_num = int(input( "Enter a number between 0 and 4: "))
end_num = int(input( "Enter a number between 5 and 9: "))
print(colors_list[strt_num:end_num])'''


'''Task 75

num_list = [123, 456, 789, 321]
for i in num_list:
    print(i)
rannum = int(input("Please enter a three-digit number: "))
if rannum in num_list:
    print(rannum, "has an index", num_list.index(rannum))
else:
    print("Not in the list")'''


'''Task 76'''
'''invitees = []
for i in invitees [0,2]:
    invitee.append(input("Add a name:"))
extra = input("Do you want to add another name?")
if answer == "Yes":
    invitees = +1
else:
    print(len(invitees))'''


'''invitee1 = input("Enter a name of smb you want to invite to the party: ")
invitee2 = input("Enter another name: ")
invitee3 = input("Enter a third name: ")

party = [invitee1, invitee2, invitee3]
extra = input("Do you want to add another name? (y/n): ")

while extra == "y":
    new_invitee = party.append(input("Enter another name: "))
    extra = input("Do you want to add another name? (y/n): ")

print("You have", len(party), "people coming to your party")'''


'''Task 77

invitee1 = input("Enter a name of smb you want to invite to the party: ")
invitee2 = input("Enter another name: ")
invitee3 = input("Enter a third name: ")

party = [invitee1, invitee2, invitee3]
extra = input("Do you want to add another name? (y/n): ")

while extra == "y":
    new_invitee = party.append(input("Enter another name: "))
    extra = input("Do you want to add another name? (y/n): ")

print("You have", len(party), "people coming to your party")

print(party)

name = input("Please type in one of the name of the invitees: ")
print(name, "has index number", party.index(name))
stillcome = input("Do you still want them to come to the party? y/n: ")
if stillcome == "n":
    party.remove(name)

print(party)'''


'''Task 78
tv_programs = ["Bingo", "Zondag met L", "Love Island", "Dr Who"]

for i in tv_programs:
    print(i)

show_name = input("Please add another show: ")
position = int(input("Please enter a posisition ypu want to insert it in from 0 to 3: "))

tv_programs.insert(position, show_name)

print(tv_programs)'''

'''Task 079'''
'''nums = []

num1 = input("Please enter a number:")
nums.append(num1)
print(nums)
num2 = input("Please enter a number:")
nums.append(num2)
print(nums)
num3 = input("Please enter a number:")
nums.append(num3)
print(nums)

extra = input("Do you still want the last number saved? y/n: ")
if extra == "n":
    nums.remove[2]

print(nums)'''


'''nums = []
count = 0
while count <3:
    num = int(input("Enter a number: "))
    nums.append(num)
    print(nums)
    count = count + 1
lastnum = input("Do you still want the last number saved? y/n: ")
if lastnum == "n":
    nums.remove(num)
print(nums)'''
