import requests

class Book:
    def __init__(self, title, author, isbn, copies=1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies
        self.borrowed = 0

    def is_available(self):
        return (self.copies - self.borrowed) > 0

    def borrow(self):
        if not self.is_available():
            raise ValueError("No copies available")
        self.borrowed += 1

    def return_book(self):
        if self.borrowed == 0:
            raise ValueError("No borrowed copies to return")
        self.borrowed -= 1

    def available_copies(self):
        return self.copies - self.borrowed


class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}

    def add_book(self, book):
        if book.isbn in self.books:
            raise ValueError("Book already exists")
        self.books[book.isbn] = book

    def remove_book(self, isbn):
        if isbn not in self.books:
            raise ValueError("Book not found")
        del self.books[isbn]

    def find_book(self, isbn):
        if isbn not in self.books:
            raise ValueError("Book not found")
        return self.books[isbn]

    def total_books(self):
        return len(self.books)

    def fetch_book_info(self, isbn):
        response = requests.get(f"https://api.bookinfo.com/books/{isbn}")
        data = response.json()
        return data["title"]