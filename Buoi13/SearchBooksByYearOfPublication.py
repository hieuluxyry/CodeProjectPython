import sqlite3
def get_books_published_after(year):
    with sqlite3.connect("BookInfo.db") as db:
        cursor = db.cursor()
        query = """
        SELECT Title, Author, DatePublished
        FROM Book
        WHERE DatePublished > ?
        ORDER BY DatePublished
        """
        cursor.execute(query, (year,))
        books = cursor.fetchall()
        if books:
            print(f"\nCác cuốn sách được xuất bản sau năm {year}:")
            for book in books:
                print(f"Tiêu đề: {book[0]}, Tác giả: {book[1]}, Năm xuất bản: {book[2]}")
        else:
            print(f"Không có sách nào được xuất bản sau năm {year}.")
user_input = input("Nhập năm để tìm sách xuất bản sau năm đó: ")
try:
    year = int(user_input)
    get_books_published_after(year)
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ cho năm.")

