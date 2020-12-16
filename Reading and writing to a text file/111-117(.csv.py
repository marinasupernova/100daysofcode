import csv

'''file = open ("Stars.csv", "w")
new_record = "Brian, 73, Taurus\n"
file.write(str(new_record))
file.close()

file = open ("Stars.csv", "r")
print(file.read())'''




'''file = open("Stars.csv", "a")

name = input("Enter a name:")
age = input("Enter age: ")
star = input("Enter a star sign: ")

new_record = name + "," + age + "," + star + "\n"

file.write(str(new_record))
file.close()'''



# opens in a read mode and display the record one row at time

'''file = open("Stars.csv", "r")
for row in file:
    print(row)'''


#displays only row 1
'''file = open("Stars.csv", "r")
reader = csv.reader(file) # Return a reader object which will iterate over lines in the given csvfile.
rows = list(reader) # list() - return a list
print(rows[1])'''



'''file = open ("Stars.csv", "r")

search = input("Enter the data you are searching for: ")
reader = csv.reader(file)

# displys all the rows that contain that data anywhere in the row
for row in file:  
    if search in str(row):
        print(row)'''

'''
file = list(csv.reader(open("Stars.csv")))

tmp = []

for row in file:
    tmp.append(row)
'''



'''
file = open("NewStars.csv", "w")
x = 0

for row in tmp:
    new_record = tmp[x][0] + " , " + tmp[x][1] + " , " +tmp[x][2] + "\n"
    file.write(new_record)
    x = x + 1
file.close()
'''

'''Task 111

file = open("Books.csv", "w")
new_record = " To Kill A Mockingbird, Harper Lee, 1960\n A Brief History of Time, Stephen Hawking, 1988\n The Great Gatsby, F. Scott Fitzgerald, 1922 \n The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n Pride and Prejudice, Jane Austen, 1813"
file.write(str(new_record))
file.close()


file = open ("Books.csv", "r")
print(file.read())'''


'''Task 112


name = input("Enter a name of the book: ")
author = input("Enter an author of the book: ")
year = input("Enter a year of the book: ")

new_record = "\n" + " " + name + " , " + author + " , " + str(year)

file = open("Books.csv", "a")
file.write(new_record)
file.close


file = open ("Books.csv", "r")
for row in file:
    print(row)
file.close()'''


'''Task 113'''

#add an author
'''num = int(input("How many books do you want to add to the list?"))
file = open("Books.csv", "a")

for x in range (0, num):
    name = input("Enter a name of the book: ")
    author = input("Enter an author of the book: ")
    year = input("Enter a year it was released: ")
    new_record = "\n" + " " + name + " , " + author + " , " + str(year) + "\n"

file.close()

#search for an author

search_author = input("Please enter an author's name to search: ")

file = open("Books.csv", "r")
count = 0
for row in file: 
    if search_author in str(row):
        print(row)
        count = count + 1
if count == 0:
    print("There are no books by that author in this list")

file.close()'''

'''Task 114'''

'''
start_year = str(input("Please enter a start year of release: "))
end_year = str(input("Please enter an end year of release: "))

file = open("Books.csv", "r")
reader = csv.reader(file)

for xxx in file:  
    if start_year and end_year in str(row):
        print(row)
'''

'''
file = open(“NewStars.csv”,“w”)
for row,i in tmp:
    newRec = tmp[i][0] + ”,” + tmp[i][1] + ”,” + tmp[i][2] + ”\n”
    file.write(newRec)
file.close()
'''
'''
Task 114
start_year = int(input("Please enter a start year of release: "))
end_year = int(input("Please enter an end year of release: "))

file_pointer = open("Books.csv", "r")
reader = csv.reader(file_pointer) # читает файл построчно
books = list(reader) # а это мы из него сделали список чтобы с ним работать 

books_list = [] #сюда мы будем записывать список книг подходящий


length = len(books)

i = 0

while i < length: 
    if int(books[i][2]) >= start_year and int(books[i][2]) <= end_year:
        books_list.append(books[i])
    i += 1

print(books_list)

''' 

'''Task 115

file  = open("Books.csv", "r")
reader = list(csv.reader(file))

length = len(reader)
books = []
i = 0

while i < length:
    display = "Row: " + str(reader[i])
    i += 1
    print(display, i) # как чтоб в начале

'''





