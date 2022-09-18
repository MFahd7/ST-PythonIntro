def append(str):
    try:
        file1 = open("list.txt", "a")
    except Exception as e:
        print(e)
        return False
    else:
         file1.write(str)
         file1.close()
         return True

def read():
    try:
        f = open('list.txt', 'r')
    except Exception as e:
        print("-------- error -----------")
        return False
    else:
        userinfo = f.readlines()
        return userinfo



def askuser(mes):
    Uinput = input(mes)
    if Uinput.isalpha():
        return Uinput

    print("-- inavlid input --")
    return askuser(mes)

def email(mes):
    em = input(mes)
    import re
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(regex, em):
        print("valid email")
        return em

    print("---- wrong email ----")
    return email(mes)

import time
def generteid():
    id = round(time.time())
    return id



def regUser():
    print("register new user: ")
    fname = askuser("enter firstname: ")
    lname = askuser("enter last name: ")
    emal = email('enter email:')
    id = generteid()
    userinfo = f"{id}:{fname}:{lname}:{emal}\n"
    created = append(userinfo)
    if created:
        print("--- added successfully --")
        return created

def display():
    print("--- all users ---\n")
    users = read()
    for user in users:
        print(user)



def menu():
    res = input("if you want to register press R, if you want list the users press L, or press E to exit: ")
    if res == "r":
        add = regUser()
        return menu()

    elif res == 'l':
        display()
        return menu()

    elif res == 'e':
        print('  ---- good bye ----  ')

    else:
        print("----------- inavlid choice --------------")
        return menu()


menu()
