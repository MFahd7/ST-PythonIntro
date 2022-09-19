import os
import time
import json
import re


def main():

    if not os.path.isfile("data.json"):

        with open("data.json", 'w', encoding='utf-8', errors="") as file:
            file.write("{}")

    while True:
        letter = input("Please enter:- r for register\n l for listing\n d for delete\n e for exit --> ")

        if letter == "l":
            show_users()

        elif letter == "r":
            regUser()

        elif letter == "d":
            delUser()

        elif letter == "e":
            print("\n --- gd bye ---")
            break

        else:
            print("Invalid input.")


def regUser():
    firstname = input("Please enter firstname: ")
    lastname = input("Please enter lastname: ")
    email = Email()
    user_id = generate_id()

    print(firstname, lastname, email, user_id)

    with open("data.json", 'r', encoding='utf-8', errors="") as f:
        users = json.load(f)
        users[user_id] = {"firstname": firstname, "lastname": lastname, "email": email}

    with open("data.json", 'w', encoding='utf-8', errors="") as obj:
        obj.write(json.dumps(users))


def delUser():
    user_id = input("Enter user ID: ")

    with open("data.json", 'r', encoding='utf-8', errors="") as f:
        users = json.load(f)

        if user_id in users.keys():
            users.pop(user_id)
            print("User deleted!")

        else:
            print("User does not exist.")

    with open("data.json", 'w', encoding='utf-8', errors="") as o:
        o.write(json.dumps(users))


def show_users():
    print("users list")
    users = get_users()

    for user in users.keys():
        messege = f"{{id: {user}, " + str(users[user])[1:]
        print(messege)


def get_users():

    with open("data.json", 'r', encoding='utf-8', errors="") as f:
        return json.load(f)


def Email():
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    while True:
        email = input("Please enter your email: ")

        if re.fullmatch(regex, email):
            return email


def generate_id():
    user_id = round(time.time())
    return user_id


main()
