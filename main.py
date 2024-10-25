def login(credential):
    password = credential['password']
    if password == 123:
        print("Login successfull")
    else:
        print("Invalid login")

my_dictionary = {"name":"Jen"}
login(my_dictionary)