# Search for a book by title 

def search_book(library):
    print("What book are you searching for")
    title=input("What is the Title of the book: ")
    if title in library:
        print(f"Book  {library[title]} ")
    else:
        print("Book not found")
        