import sqlite3

with sqlite3.connect("Bookinfo.db") as db:
    cursor = db.cursor()

cursor.execute("SELECT * FROM Authors ")
for x in cursor.fetchall():
    print(x)

place_ofbirth = input("Please enter a place of birth: ")

cursor.execute("""SELECT Books.Title,Books.Date_Published,Books.Author
    FROM Books, Authors WHERE Authors.Name=Books.Author AND Authors.PlaceofBirth=?""", [place_ofbirth])

for x in cursor.fetchall():
    print(x)

db.close()