print("📖 Welcome to the library application!")

def print_commands():
    print("Commands:")
    print("\t1) List books")
    print("\t2) Add a book")
    print("\t3) Edit a book")
    print("\t4) Delete a book")
    print("\t5) List authors")
    print("\t6) Add an author")
    print("\t7) Exit application")

def list_books():
    pass

def add_book():
    name = input("Name:")
    year = input("Year:")
    genres = input("Genres (comma separated):")
    copies = input("Number of copies:")
    author = input("Author ID:")
    
    # Save the book to the database
    
    print(f"Book {name} has been added!")

def edit_book():
    pass

def delete_book():
    pass

def list_authors():
    pass

def add_author():
    pass

print_commands()

while True:
    command = input("Type in the command number:")
    
    if command == "1":
        list_books()
    elif command == "2":
        add_book()
    elif command == "3":
        edit_book()
    elif command == "4":
        delete_book()
    elif command == "5":
        list_authors()
    elif command == "6":
        add_author()
    elif command == "7":
        break
    else:
        print("I don't know that command")

print("Goodbye!")

    
    