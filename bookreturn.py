# returns book
library=[]
def book_return(library):
    title= input("Enter the book you wish to return: ")
    if title in library:

        library[title]["Availability"]="available"
        library[title]["User"]="None"
        library.update(library.copy())
        print((title), "has been changed to 'available'")
    else:
        print("Book not found")
        