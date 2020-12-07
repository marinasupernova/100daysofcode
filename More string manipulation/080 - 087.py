'''msg = "MARINA"


if msg.isupper():
    print("Uppercase")
else:
    print("This is not in uppercase")


msg.islower()'''

'''msg = "Hello"
for letter in msg:
    print(letter, end="*")'''


'''Task 080

name = input("Please enter your name: ")
print("That has", len(name), "characters in it")
surname = input("Please enter your surname: ")
print("That has", len(surname), "characters in it")
together = name + " " + surname
print("Your full name is", together)
print("That has", len(together), "characters in it")'''


'''Task 081

subject = input("What is your favourite school subject? ")
for letter in subject:
    print(letter, end="-")'''

'''Task 082

poem = "To be or not to be that is the question"
start = int(input("Please enter a starting point: "))
end = int(input("Please enter an ending point from 0 till 39: "))
print(poem[start:end])'''


'''Task 083

word = input("Please type a word in upper case: ")
tryagain = False
while tryagain == False:
    if word.isupper:
        print("Well done!")
        tryagain = True
    else:
        print("THis is not an upper case. Try again!")
        word = input("Please type a word in upper case: ")'''





'''Task 084

postcode = input("Please enter your postcode: ")
end = postcode[4:6]
print(end.upper())'''


'''Task 085


name = input("Please enter your name: ")

vowelcount = 0
name = name.lower()

for i in name: 
    if i == "a" or i == "o" or i == "u" or i == "e" or  i == "i":
        vowelcount = vowelcount +1
print("THere are", vowelcount, "vowels in your name")'''



'''Task 086

password1 = input("Please enter a password: ")
password2 = input("Please enter a password again: ")

if password1 == password2:
    print("Thank you!")
elif password1.islower() == password2.islower():
    print("They must be the same case")
else:
    print("Incorrect")'''


Task087

word = input("Please enter a word: ")
length = len(word)
num = 1
for i in word:
    position = length - num
    letter = word[position]
    print(letter)
    num = num+1'''



