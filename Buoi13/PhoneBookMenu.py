import  sqlite3
def view_phonebook(cursor):
    cursor.execute("SELECT * FROM PhoneBook")
    rows = cursor.fetchall()
    if rows :
        for row in rows :
            print(row)
    else:
        print("Danh bạ Trống Rỗng ")
def add_person(cursor):
    newID = input("Nhập ID: ")
    newFirstName = input("Nhập FirstName: ")
    newSurname = input("Nhập Surname: ")
    newPhoneNumber = input("Nhập Phone Number: ")
    cursor.execute("""INSERT INTO PhoneBook(ID, FirstName, Surname, PhoneNumber) 
                      VALUES(?, ?, ?, ?)""",(newID, newFirstName, newSurname, newPhoneNumber))
def search_by_surname(cursor):
    surname = input("Nhập Surname để tìm kiếm: ")
    cursor.execute("SELECT * FROM PhoneBook WHERE Surname = ?", (surname,))
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print(f"Không tìm thấy tên phù hợp '{surname}'.")
def delete_by_id(cursor):
    id_to_delete = input("Nhập ID để xóa: ")
    cursor.execute("DELETE FROM PhoneBook WHERE ID = ?", (id_to_delete,))
    if cursor.rowcount > 0:
        print(f" ID {id_to_delete} đã số thành công .")
    else:
        print(f" Không tìm thấy ID như bạn cung cấp{id_to_delete}.")
def display_menu():
    print("\nPhoneBook Menu")
    print("1. Hiển thị danh sách PhoneBook")
    print("2. Thêm người vào danh sách Phone Book")
    print("3. Tìm kiếm theo tên ")
    print("4. Xoá ID ")
    print("5. Thoát Chương trình ")
def main () :
    import sqlite3
with sqlite3.connect("PhoneBook.db") as db:
    phone=db.cursor()
phone.execute("""CREATE TABLE IF NOT EXISTS PhoneBook(
ID integer PRIMARY KEY,
FirstName text NOT NULL,
Surname text NOT NULL,
PhoneNumber integer);""")
while True :
    display_menu()
    choice_menu = input(" Mời nhập lựa chọn từ 1 - 5 : ")
    if choice_menu == '1':
        view_phonebook(phone)
    elif choice_menu == '2':
        add_person(phone)
        db.commit()
    elif choice_menu == '3':
        search_by_surname(phone)
    elif choice_menu == '4':
        delete_by_id(phone)
        db.commit()
    elif choice_menu== '5':
        print("Thoát Chương Trình .")
        break
    else:
        print("Vui lòng chọn đúng số lựa chọn hợp lệ")
