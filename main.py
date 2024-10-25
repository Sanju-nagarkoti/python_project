def login(credential):
    password = credential.get('password')
    if password==None:
        print("password doesn't exist")
    
    elif password == 123:
        print("Login successfull")
    else:
        print("Invalid login")

my_dictionary = {"name":"Jen"}
login(my_dictionary)