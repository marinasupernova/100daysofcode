# import sqlite3

# with sqlite3.connect("company.db") as db:
#     cursor = db.cursor()

# cursor.execute(""" CREATE TABLE IF NOT EXISTS employees(
#     id integer PRIMARY KEY,
#     name text NOT NULL,
#     dept text NOT NULL,
#     salary integer); """)

# cursor.execute(""" INSERT INTO employees(id,name,dept,salary)
#     VALUES("5", "BOB", "Sales", "25000")""")
# db.commit()

# newID = input("Enter ID number: ")
# new_name = input("Enter a name ")
# new_dept = input("Enter department: ")
# new_salary = input("Enter salary: ")
# cursor.execute(""" INSERT INTO employees(id, name, dept, salary)
#     VALUES(?, ?, ?, ?) """, (newID, new_name, new_dept, new_salary))

# db.commit()

# cursor.execute("SELECT * FROM employees ")
# print(cursor.fetchall())


# cursor.execute("SELECT * FROM employees")
# for x in cursor.fetchall():
#     print(x)

# cursor.execute("SELECT * FROM employees ORDER BY name")
# for x in cursor.fetchall():
#     print(x)

# cursor.execute("SELECT * FROM employees WHERE salary > 20000")

# cursor.execute("SELECT * FROM employees WHERE dept='Sales'")

# cursor.execute("""SELECT employees.id,employees.name
#     FROM employees.dept WHERE employees.salary >20000 """)

# cursor.execute("SELECT id, name, salary FROM employees")


# whichDept = input("Enter a department: ")
# cursor.execute("SELECT * FROM employees WHERE dept=?", [whichDept])

# cursor.execute(""" SELECT employees.id, employees.name,dept.manager
#     FROM employees,dept WHERE employees.dept = dept.dept""")


# cursor.execute("UPDATE employees SET name = 'Tony' WHERE id =1")
# db.commit()

# cursor.execute("DELETE employees WHERE id=1")
# db.close()


# for x in cursor.fetchall():
# #     print(x)

# db.close()


'''Task 139 -140'''

# import sqlite3

# with sqlite3.connect("PhoneBookmain.db") as db:
#     cursor = db.cursor()

# cursor.execute(""" CREATE TABLE IF NOT EXISTS Names(
#     id integer PRIMARY KEY,
#     name text NOT NULL,
#     surname text NOT NULL,
#     phonenumber integer); """)

# cursor.execute(""" INSERT INTO Names(id, name, surname, phonenumber)
#     VALUES("1", "Simon", "Howels", "011223 3497752")""")
# db.commit()

# cursor.execute(""" INSERT INTO Names(id, name, surname, phonenumber)
#     VALUES("2", "Karen", "Phillips", "01954 295773" )""")
# db.commit()

# cursor.execute(""" INSERT INTO Names(id, name, surname, phonenumber)
#     VALUES("3", "Darren", "Smith", "01583 749012" )""")
# db.commit()

# cursor.execute(""" INSERT INTO Names(id, name, surname, phonenumber)
#     VALUES("4", "Anne", "Jones", "01323 567322" )""")
# db.commit()

# cursor.execute(""" INSERT INTO Names(id, name, surname, phonenumber)
#     VALUES("5", "Mark", "Smith", "01223 855534" )""")
# db.commit()

# db.close()




# def display_phonebook():
#     cursor.execute("SELECT * FROM Names")
#     for x in cursor.fetchall():
#         print(x)

# def add_to_phb():
#     new_id = input("Please enter an ID number :")
#     new_name = input("Please enter a name :")
#     new_surname = input("Please enter a surname :")
#     new_phonenumber = input("Please enter an phone number :")
#     cursor.execute(""" INSERT INTO Names (id, name, surname, phonenumber)
#         VALUES(?, ?, ?, ?) """, (new_id, new_name, new_surname, new_phonenumber))
#     db.commit()

# def show_surname():
#     selected_surname = input("Please enter a surname: ")
#     cursor.execute("SELECT * FROM Names WHERE surname =?", [selected_surname])
#     for x in cursor.fetchall():
#         print(x)


# def delete_byid():
#     selected_id = int(input("Please select an id: "))
#     cursor.execute("DELETE FROM Names WHERE id =?", [selected_id])
#     cursor.execute("SELECT * FROM Names")
#     for x in cursor.fetchall():
#         print(x)
#     db.commit()


# def main():
#     again = "y"
#     while again == "y":
#         print("""Main Menu:

#         1) View Phone Book 
#         2) Add to Phone Book
#         3) Search for surnames
#         4) Delete "person from Phone Book
#         5) Quit """)

#         user_input = int(input("Enter your selection: "))
    
#     if user_input == 1:
#         display_phonebook()

#     elif user_input == 2:
#         add_to_phb()

#     elif user_input == 3:
#         show_surname()

#     elif user_input == 4:
#         delete_byid()

#     elif user_input == 5:
#         again = "n"

#     else:
#         print("Enter a number from the selection above")


# main()
# db.close()

'''Task 142'''

import sqlite3





# import sqlite3

# with sqlite3.connect("PhoneBookmain.db") as db:
#     cursor = db.cursor()