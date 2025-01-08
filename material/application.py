print("📖 Welcome to the library application!")

def print_commands():
    print("Commands:")
    print("\t1) List books")
    print("\t2) Add a book")
    print("\t3) Edit a book")
    print("\t4) Delete a book")
    print("\t7) Exit application")

def list_books():
    # Fetch all the books from the database and print their information
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
    # Update book's information based on user's input
    pass

def delete_book():
    # Delete a book based on user's input
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
    elif command == "7":
        break
    else:
        print("I don't know that command")

print("Goodbye!")

    
    