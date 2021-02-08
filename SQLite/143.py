import sqlite3

with sqlite3.connect("Bookinfo.db") as db:
    cursor = db.cursor()


year_published = int(input("Please enter a year the book was published: "))

cursor.execute(""" SELECT Books.Title, Books.Date_Published, Books.Author
    FROM Books WHERE Books.Date_Published>?""", [year_published])

for x in cursor.fetchall():
    print(x)

db.close()