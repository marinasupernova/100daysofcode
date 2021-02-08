import sqlite3
file = open("Booklist.txt", "w")

with sqlite3.connect("Bookinfo.db") as db:
    cursor = db.cursor()

cursor.execute("SELECT Name from Authors")
for x in cursor.fetchall():
    print(x)  

authors_name = input("Please enter an author's name:")
print()

cursor.execute("SELECT * FROM Books WHERE Author=?",[authors_name])
for x in cursor.fetchall():
    new_record = str(x[0]) + " - " + x[1] + " - " + x[2] + " - " + str(x[3]) + "\n"
    file.write(new_record)

file.close()
db.close()
