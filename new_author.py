#adds new author

author=[]
def new_author_name(author):
    
    author_name=input("What is the name of the author you want to add: ")
    author_city=input("What city was the author born: ")
    author_books=input("What book have they written: ")
    author[author_name]={"Author":author_name,"Birthplace":author_city,"Books":author_books}
    new_author=(author)
    author.update(new_author.copy())
   
     
   
def display_authors(author):
    display=(author)
    print(display)
        
        
    