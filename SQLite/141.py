# '''Task 142'''

import sqlite3

with sqlite3.connect("Bookinfo.db") as db:
    cursor = db.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS Authors(
#     Name text PRIMARY KEY,
#     PlaceofBirth text NOT NULL);""")

# cursor.execute("""INSERT INTO Authors(Name, PlaceofBirth)
#     VALUES("Agatha Christie", "Torquay")""")
# db.commit()

# cursor.execute(""" INSERT INTO Authors(Name, PlaceofBirth)
#     VALUES("Cecelia Ahern", "Dublin")""")
# db.commit()

# cursor.execute(""" INSERT INTO Authors(Name, PlaceofBirth)
#     VALUES("J. Rowling", "Bristol")""")
# db.commit()

# cursor.execute(""" INSERT INTO Authors(Name, PlaceofBirth)
#     VALUES("Oscar Wilde", "Dublin")""")
# db.commit()


# cursor.execute(""" CREATE TABLE IF NOT EXISTS Books(
#     id integer PRIMARY KEY,
#     Title text NOT NULL,
#     Author text NOT NULL,
#     Date_Published integer NOT NULL);""")


# cursor.execute("""INSERT INTO Books(id, Title, Author, Date_Published)
#     VALUES("1", "De Produndis", "Oscar Wilde", "1905")""")
# db.commit()

# cursor.execute("""INSERT INTO Books(id, Title, Author, Date_Published)
#     VALUES("2", "Harry Potter and the Chanber of Secrets", "J. Rowling", "1998")""")
# db.commit()

# cursor.execute("""INSERT INTO Books(id, Title, Author, Date_Published)
#     VALUES("3", "Harry Potter and the Prisoner of Azkaban", "J. Rowling", "1999")""")
# db.commit()

# cursor.execute("""INSERT INTO Books(id, Title, Author, Date_Published)
#     VALUES("4", "Lyrebird", "Cecelia Ahern", "2017")""")
# db.commit()

# cursor.execute("""INSERT INTO Books(id, Title, Author, Date_Published)
#     VALUES("5", "Murder on the Orient Express", "Agatha Cristie", "1934")""")
# db.commit()

# cursor.execute("""INSERT INTO Books(id, Title, Author, Date_Published)
#     VALUES("6", "Perfect", "Cecelia Ahern", "2017")""")
# db.commit()

# cursor.execute("""INSERT INTO Books(id, Title, Author, Date_Published)
#     VALUES("7", "The Marble Collector", "Cecelia Ahern", "2016")""")
# db.commit()

# cursor.execute("""INSERT INTO Books(id, Title, Author, Date_Published)
#     VALUES("8", "The Murder on the links", "Agatha Cristie", "1923")""")
# db.commit()

# cursor.execute("""INSERT INTO Books(id, Title, Author, Date_Published)
#     VALUES("9", "The picture of Dorian Grey", "Oscar Wilde", "1890")""")
# db.commit()

# cursor.execute("""INSERT INTO Books(id, Title, Author, Date_Published)
#     VALUES("10", "The secret adversary", "Agatha Cristie", "1921")""")
# db.commit()

# cursor.execute("""INSERT INTO Books(id, Title, Author, Date_Published)
#     VALUES("11", "The seven dials mystery", "Agatha Cristie", "1929")""")
# db.commit()

# cursor.execute("""INSERT INTO Books(id, Title, Author, Date_Published)
#     VALUES("12", "The Year I met you", "Cecelia Ahern", "2014")""")
# db.commit()


cursor.execute("SELECT Author FROM Books")
for x in cursor.fetchall():
    print(x)