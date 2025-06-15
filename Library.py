
class Book:
    def __init__(self, author="", title="", num_of_pages=0):
        self.author = author
        self.title = title
        self.num_of_pages = num_of_pages


class Shelf:
    def __init__(self):
        self.is_shelf_full = False
        self.books = []
        self.max_books_in_shelf = 5

    def add_book(self, new_book):
        if isinstance(new_book, Book):
            if len(self.books) >= self.max_books_in_shelf:
                print("There is no free space on the shelf.")
                self.is_shelf_full = True
                return False
            else:
                self.books.append(new_book)
                self.is_shelf_full = len(self.books) == self.max_books_in_shelf
                return True

    def replace_book(self, pos1, pos2):
        if pos1 < 1 or pos1 > 5 or pos2 < 1 or pos2 > 5:
            print("invalid positions. Must be between 1 and 5")
            return False
        i1 = pos1 - 1
        i2 = pos2 - 1

        if i1 >= len(self.books) or i2 >= len(self.books):
            print("One or both positions are empty.")
            return False

        temp = self.books[i1]
        self.books[i1] = self.books[i2]
        self.books[i2] = temp
        print("The books swapped successfully.")


class Reader:
    def __init__(self, reader_id=0, name=""):
        self.reader_id = reader_id
        self.name = name
        self.books_read = []

    def read_book(self, title=""):
        if isinstance(title, str):
            self.books_read.append(title)
        else:
            print("Enter a book name please...")


class Library:
    def __init__(self):
        self.shelves = []
        for _ in range(3):
            self.shelves.append(Shelf())

        self.readers = []

    def is_there_place_for_new_book(self):
        for shelf in self.shelves:
            if len(shelf.books) < shelf.max_books_in_shelf:
                return True
        return False

    def add_new_book(self, new_book):
        for shelf in self.shelves:
            if shelf.add_book(new_book):
                print(f"Book '{new_book.title}' added successfully.")
                return True
        print("All shelves are full. Cannot add book.")

    def delete_book(self, title):
        for shelf in self.shelves:
            for book in shelf.books:
                if book.title == title:
                    shelf.books.remove(book)
                    shelf.is_shelf_full = len(
                        shelf.books) == shelf.max_books_in_shelf
                    print(f"Book {title} deleted.")
                    return True
        print(f"Book {title} not found.")

    def register_reader(self, name, reader_id):
        for reader in self.readers:
            if reader.reader_id == reader_id or reader.name == name:
                print("Reader already exists.")
            return
        self.readers.append(Reader(reader_id, name))
        print(f"Reader {name} registered.")

    def remove_reader(self, name):
        for reader in self.readers:
            if reader.name == name:
                self.readers.remove(reader)
                print(f"Reader {name} removed.")
                return True
        print(f"Reader {name} not found.")

    def search_by_author(self, author):
        titles = []
        for shelf in self.shelves:
            for book in shelf.books:
                if book.author.lower() == author.lower():
                    titles.append(book.title)
        return titles
