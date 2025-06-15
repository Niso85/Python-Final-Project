from Library import Book, Shelf, Reader, Library

library = Library()

for shelf in library.shelves:
    shelf.add_book(Book("Haim Nahman", "Shirat Habarboor", 100))
    shelf.add_book(Book("Moshe Zoohmir", "LLelot Levanim", 1000))


while True:
    print("\nWelcome to the Library!")
    print("For adding a book - Press 1")
    print("For deleting a book - Press 2")
    print("For registering a new reader - Press 3")
    print("For removing a reader - Press 4")
    print("For searching books by author - Press 5")
    print("For exit - Press 6")

    choice = input("Enter your choice number between 1 and 6: ")

    if choice == "1":
        title = input("Enter the book title: ")
        author = input("Enter the book author: ")
        if not title or not author:
            print("Author and title cannot be empty.")
            continue
        try:
            pages = int(input("Enter number of pages: "))
        except ValueError:
            print("Page number must be an integer.")
            continue

        new_book = Book(author, title, pages)
        library.add_new_book(new_book)

    elif choice == "2":
        title = input("Enter the title of the book to delete: ")
        if not title:
            print("Title cannot be empty.")
            continue
        library.delete_book(title)

    elif choice == "3":
        name = input("Enter reader's name: ")
        if not name:
            print("Name cannot be empty.")
            continue
        try:
            reader_id = int(input("Enter reader ID (number): "))
        except ValueError:
            print("Reader ID must be a number.")
            continue
        library.register_reader(name, reader_id)

    elif choice == "4":
        name = input("Enter the name of the reader to remove: ")
        if not name:
            print("Name cannot be empty.")
            continue
        library.remove_reader(name)

    elif choice == "5":
        author = input("Enter author name to search for: ").strip()

        if not author:
            print("Author name cannot be empty.")
            continue

        titles = library.search_by_author(author)

        if titles:
            print(f"\nBooks by {author}:")
            for title in titles:
                print(" -", title)
        else:
            print(f"No books found by author {author}.")

    elif choice == "6":
        print("Exiting the Library System. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a number between 1 and 6.")
