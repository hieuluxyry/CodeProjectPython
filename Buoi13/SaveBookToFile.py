import sqlite3
with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()
    author_name = input("Enter the author's name: ")
    cursor.execute("SELECT * FROM Book WHERE Author=?", (author_name,))
    books = cursor.fetchall()
    file_name = f"{author_name}_books.txt"
    with open(file_name, "w") as file:
        for book in books:
            book_info = "-".join(str(field) for field in book)
            file.write(book_info + "\n")
print(f"Books by {author_name} have been saved to '{file_name}'.")