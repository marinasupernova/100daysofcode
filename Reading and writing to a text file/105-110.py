'''file = open("Countries.txt", "w")
file.write("Italy\n")
file.write("Germany\n")
file.write("Spain\n")
file.close()

file = open("Countries.txt", "r")
print(file.read())


file = open("Countries.txt", "a")
file.write("France\n")
file.close()'''



'''Task 105


file = open("Numbers.txt", "w")
file.write("1,")
file.write("2,")
file.write("3,")
file.write("4,")
file.write("5.")
file.close()

file = open("Numbers.txt", 'r')
print(file.read())'''


'''Task 106 -107


file = open("Names.txt", "w")
file.write("Nicol\n")
file.write("Charlotte\n")
file.write("Emy\n")
file.write("Cassandra\n")
file.write("Michelle\n")
file.close()

file = open("Names.txt", "r")
print(file.read())  # как он знает что строка 44 относится к строке 43 и как он згает какой файл чиатть '''



'''Task 108

file = open("Names.txt", "a")
new_name = input("Pleae enter a name:")
file.write(new_name + "\n")
file.close()

file = open("Names.txt", "r")
print(file.read())
file.close()'''


'''Task 109


print("1. Create a new file")
print("2. Display the file")
print("3. Add a new item to the file")
print("Make a selection 1, 2, 3")

selection = int(input("Please enter 1,2 or 3: "))

if selection == 1 :
    subject = input("Enter a school subject: ")
    file = open("School subjects.txt", "w")
    file.write(subject + "\n")
    file.close()
elif selection == 2:
    file = open("School subjects.txt", "r")
    print(file.read())
elif selection == 3:
    new_subject = input("Please enter a new subject: ")
    file = open("School subjects.txt", "a")
    file.write(new_subject + "\n")
    file.close()
    file = open("School subjects.txt", "r")
    print(file.read())
else:
    print("Out of range")'''



''' Task 110

file = open("Names.txt", "r")
print(file.read())

file = open("Names.txt", "r")
selection = input("Please select one of the names: ")
selection = selection + "\n"

for row in file:
    if row!= selection:
        file = open("Names2.txt", "a")
        newrecord = row
        file.write(newrecord)
        file.close()

file.close()

file = open("Names.txt", "r")
print(file.read())

file = open("Names2.txt", "r")
print(file.read())'''






