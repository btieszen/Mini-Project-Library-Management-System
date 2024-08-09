#adds new user

user=[]
def add_new_user(user):

    user_name= input("What is the name of the user:  ")
    user_id = input("What is their new library ID: ")
    user[user_name]={"Name":user_name,"Id":user_id}
    new_users=(user)
    user.update(new_users.copy())
    

 
def display_user(user):
   user1=user
   print(user1)
    
    
