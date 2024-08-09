#marks books as borrowed


def get_borrowed_book(library):
    title= input("Enter the book you wish to borrow: ")
    new_user =input("Who is borrowing the book: ")
    if title in library:
        
        library[title]["Availability"]="Borrowed"
        library[title]["User"]=(new_user)
     
        library.update(library.copy())
        print((title), "has been changed to 'Borrowed'")
        #user=library.update(library.copy())
    else:
        print("Book not available or not found")
def borrowed_user(library):
    print("")
def get_borrowed_user(library):
    print(library)

    
    

  

    
   

 
    

      

  
  
