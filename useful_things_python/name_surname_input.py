#Ask user for their name
def Names():
    username = ""
    name_taken = False
    while not name_taken:
        username = input("What's your name?\nMy name is ").strip().capitalize() #Remove whitespaces with strip #Start first written with big letter to name or use title() for start all other writtens.
        if len(username) > 0 and not username.isdigit():
            name_taken = True
        else:
            print("Please don't use numbers")
    return(f"Hello, {username.strip().capitalize()}")

#Ask user for their surname
def Surnames():
    surname = ""
    surname_taken = False
    while not surname_taken:
        surname = input("What's your surname?\nMy surname is ").strip().capitalize() #Remove whitespaces with strip #Start first written with big letter to surname or use title() for start all other writtens.
        if len(surname) > 0 and not surname.isdigit():
            surname_taken = True
        else:
            print("Please don't use numbers")
    return(f"{surname}! Nice to meet you.") 

print(Names(),Surnames())