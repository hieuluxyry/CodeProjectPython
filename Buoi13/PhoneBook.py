import sqlite3
with sqlite3.connect("PhoneBook.db") as db:
    phone=db.cursor()
phone.execute("""CREATE TABLE IF NOT EXISTS PhoneBook(
ID integer PRIMARY KEY,
FirstName text NOT NULL,
Surname text NOT NULL,
PhoneNumber integer);""")
db.commit()
while True :
    newID = input("Nhập ID: ")
    if  newID.lower() == 'thoat' :
        break
    newFirstName = input("Nhập FirstName: ")
    newSurname = input("Nhập Surname: ")
    newPhoneNumber = input("Nhập Phone Number: ")
    phone.execute("""INSERT INTO PhoneBook(ID, FirstName, Surname, PhoneNumber) VALUES(?,?,?,?)""", (newID, newFirstName, newSurname, newPhoneNumber))
    db.commit()
