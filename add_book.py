#adds book to library


import re
library=[]
def new_book(library):
    title =input("What is the title of the book: ")
    author=input("Who is the author: ")
    isbn=input("What is the ISBN number: ")
    if re.match(r"[A-Z][0-9]{4}",isbn):
        ISBN=(isbn)
    else:
        print("Please enter in the format Capital Letter with at least 4 numbers(A9999)")
        isbn=input("What is the ISBN number: ")
    if re.match(r"[A-Z][0-9]{4}",isbn):
        ISBN=(isbn)
        
    date=input("When was the year the book was published: ")
    if re.match(r"[0-9]{4}",date):
        publication_date=(date)
    else:
        print("Please enter in the format of only 4 numbers (2024)")
        date=input("What year was the book published: ")
    if re.match(r"[0-9]{4}",date):
        publication_date=(date)
    genre=input("What is the genre of the book: ")
    availability=("available")
    library[title] ={"Title" : title, "Author" : author, "ISBN" : isbn, "Publiction date" : publication_date,"genre" : genre,"Availability": availability}
    new_book=(library)
    library.update(new_book.copy())
    #book_new = [{"Title":(title), "Author":(author),"ISBN":(isbn)}]
    #print((book_new), "has been added.")
   
def display_books(library):
    print('')

