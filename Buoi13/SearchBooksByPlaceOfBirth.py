import sqlite3
def display_authors():
    with sqlite3.connect("BookInfo.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT NAME, PlaceOfBirth FROM Authors")
        authors = cursor.fetchall()
        if authors:
            print("Danh sách tác giả và nơi sinh của họ:")
            for author in authors:
                print(f"Tác giả: {author[0]}, Nơi sinh: {author[1]}")
        else:
            print("Không có tác giả nào trong cơ sở dữ liệu.")
def search_books_by_place_of_birth(place_of_birth):
    with sqlite3.connect("BookInfo.db") as db:
        cursor = db.cursor()
        query = """
        SELECT Book.Title, Book.DatePublished, Book.Author
        FROM Book
        JOIN Authors ON Book.Author = Authors.NAME
        WHERE Authors.PlaceOfBirth = ?
        """
        cursor.execute(query, (place_of_birth,))
        books = cursor.fetchall()
        if books:
            print(f"\nSách của các tác giả sinh ra ở {place_of_birth}:")
            for book in books:
                print(f"Tiêu đề: {book[0]}, Năm xuất bản: {book[1]}, Tác giả: {book[2]}")
        else:
            print(f"Không có sách nào của các tác giả sinh ra ở {place_of_birth}.")
display_authors()
user_input = input("\nNhập nơi sinh để tìm sách: ")
search_books_by_place_of_birth(user_input)