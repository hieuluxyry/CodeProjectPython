import sqlite3
with sqlite3.connect("BookInfo.db") as db:
    authors = db.cursor()
    authors.execute("""
    CREATE TABLE IF NOT EXISTS Authors (
        NAME TEXT PRIMARY KEY,
        PlaceOfBirth TEXT
    );
    """)
    db.commit()
    while True:
        newNAME = input("Nhập tên tác giả: ")
        if newNAME.lower() == 'thoat':
            break
        newPlaceOfBirth = input("Nhập nơi sinh tác giả: ")
        try:
            authors.execute("INSERT INTO Authors(NAME, PlaceOfBirth) VALUES(?, ?)", (newNAME, newPlaceOfBirth))
            db.commit()
        except sqlite3.IntegrityError:
            print(f"Tác giả '{newNAME}' đã tồn tại trong cơ sở dữ liệu.")
book = db.cursor()
book.execute("""
CREATE TABLE IF NOT EXISTS Book (
    ID INTEGER PRIMARY KEY,
    Title TEXT,
    Author TEXT,
    DatePublished INTEGER,
    FOREIGN KEY (Author) REFERENCES Authors(NAME)
);
""")
db.commit()
while True:
    newID = input("Nhập ID sách: ")
    if newID.lower() == 'thoat':
        break
    newTitle = input("Nhập tiêu đề sách: ")
    newAuthor = input("Nhập tên tác giả: ")
    newDatePublished = input("Nhập năm xuất bản: ")
    try:
        newID = int(newID)
        newDatePublished = int(newDatePublished)
    except ValueError:
        print("ID và năm xuất bản phải là số.")
        continue
    try:
        book.execute("INSERT INTO Book(ID, Title, Author, DatePublished) VALUES(?, ?, ?, ?)",
                     (newID, newTitle, newAuthor, newDatePublished))
        db.commit()
    except sqlite3.IntegrityError:
        print(f"Sách với ID '{newID}' đã tồn tại hoặc tên tác giả '{newAuthor}' không có trong cơ sở dữ liệu.")
