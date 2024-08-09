#gets user details


library=[]
def details_of_user(library):
    
        user_new=input("What is the name of the person you want to get details for: ")
        search_key="User"
        search_value=(user_new)
        for dictionary in library:
                if dictionary(search_key) == search_value:
                        print(library)



        
     
  
    
    
    
    
    
        

        








#filtered_list_of_dicts = [
    #dictionary for dictionary in list_of_dictionaries
    #if dictionary['name'] == 'bobby'
    
    