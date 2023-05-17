from tkinter import Button, Entry

from canvas import root, frame
from helpers import clean_screen


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
        font=15
    )

    frame.create_window(250, 270, window=register_btn)
    frame.create_window(250, 320, window=login_btn)


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
    pass


first_name_box = Entry(root, bd=0, font=15)
last_name_box = Entry(root, bd=0, font=15)
username_box = Entry(root, bd=0, font=15)
password_box = Entry(root, bd=0, font=15, show="*")
