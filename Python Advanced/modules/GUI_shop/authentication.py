from json import loads, dump
from tkinter import Button, Entry
import string

from canvas import root, frame
from helpers import clean_screen
from products_page import display_products


def get_users_data():
    info_data = []

    with open("db/user_credentials_db.txt", "r") as users_file:
        for line in users_file:
            info_data.append(loads(line))

    return info_data


def render_entry():

    register_btn = Button(
        root,
        text="Register",
        bg="green",      # Background color
        fg="white",       # Font color
        borderwidth=0,
        width=11,
        height=2,
        command=register,
        font=15
    )

    login_btn = Button(
        root,
        text="Login",
        bg="blue",  # Background color
        fg="white",  # Font color
        borderwidth=0,
        width=11,
        height=2,
        command=login,
        font=15
    )

    frame.create_window(250, 270, window=register_btn)
    frame.create_window(250, 320, window=login_btn)


# -------------------------- Registration --------------------------


def register():
    clean_screen()

    frame.create_text(180, 150, text="First name: ", font=20)
    frame.create_text(180, 200, text="Last name: ", font=20)
    frame.create_text(180, 250, text="Username: ", font=20)
    frame.create_text(180, 300, text="Password: ", font=20)

    frame.create_window(320, 150, window=first_name_box)
    frame.create_window(320, 200, window=last_name_box)
    frame.create_window(320, 250, window=username_box)
    frame.create_window(320, 300, window=password_box)

    registration_btn = Button(
        root,
        text="Register",
        font=15,
        bg="green",
        fg="white",
        command=registration
    )

    frame.create_window(250, 340, window=registration_btn)


def registration():
    user_info_dict = {
        "first_name": first_name_box.get(),
        "last_name": last_name_box.get(),
        "username": username_box.get(),
        "password": password_box.get()
    }

    if check_registration(user_info_dict):
        with open("db/user_credentials_db.txt", "a") as users_file:
            dump(user_info_dict, users_file)
            users_file.write("\n")
        display_products()


def check_registration(dict_info: dict):

    for el, value in dict_info.items():
        if value == "":

            frame.delete("error")

            frame.create_text(
                250,
                380,
                text="All field must be filled",
                font=20,
                fill="red",
                tag="error"
            )

            return False

    for char in dict_info["first_name"]:

        if char not in string.ascii_letters:

            frame.delete("error")

            frame.create_text(
                250,
                380,
                text="First name must be only letters",
                font=20,
                fill="red",
                tag="error"
            )

            return False

    for char in dict_info["last_name"]:
        if char not in string.ascii_letters:
            frame.delete("error")

            frame.create_text(
                250,
                380,
                text="Last name must be only letters",
                font=20,
                fill="red",
                tag="error"
            )

            return False

    if len(dict_info["username"]) < 6:

        frame.delete("error")

        frame.create_text(
            250,
            380,
            text="The username must be more than 5 symbols",
            font=20,
            fill="red",
            tag="error"
        )

        return False

    elif len(dict_info["username"]) > 16:

        frame.delete("error")

        frame.create_text(
            250,
            380,
            text="The username must be less than 17 symbols",
            font=20,
            fill="red",
            tag="error"
        )

        return False

    info_data = get_users_data()

    for record in info_data:
        if record["username"] == dict_info["username"]:
            frame.delete("error")

            frame.create_text(
                250,
                380,
                text="This user already exist!",
                font=20,
                fill="red",
                tag="error"
            )

            return False

    frame.delete("error")

    return True


# -------------------------- Login --------------------------


def login():
    clean_screen()

    frame.create_text(180, 250, text="Username: ", font=20)
    frame.create_text(180, 300, text="Password: ", font=20)

    frame.create_window(320, 250, window=username_box)
    frame.create_window(320, 300, window=password_box)

    login_btn = Button(
        root,
        text="Login",
        font=15,
        bg="green",
        fg="white",
        command=loging
    )

    frame.create_window(250, 340, window=login_btn)


def loging():

    if check_login():
        display_products()
    else:

        frame.create_text(
            250,
            380,
            text="Invalid username or password!",
            font=20,
            fill="red",
            tag="error"
        )


def check_login():

    info_data = get_users_data()
    user_username = username_box.get()
    user_password = password_box.get()

    for record in info_data:
        if record["username"] == user_username and record["password"] == user_password:

            return True

    return False


first_name_box = Entry(root, bd=0, font=15)
last_name_box = Entry(root, bd=0, font=15)
username_box = Entry(root, bd=0, font=15)
password_box = Entry(root, bd=0, font=15, show="*")
