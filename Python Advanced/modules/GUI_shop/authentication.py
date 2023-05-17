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
        width=15,
        height=2,
        command=register
    )

    login_btn = Button(
        root,
        text="Login",
        bg="blue",  # Background color
        fg="white",  # Font color
        borderwidth=0,
        width=15,
        height=2,

    )

    frame.create_window(250, 280, window=register_btn)
    frame.create_window(250, 320, window=login_btn)


def register():
    clean_screen()


first_name_box = Entry(root, bd=0)
last_name_box = Entry(root, bd=0)
username_box = Entry(root, bd=0)
password_box = Entry(root, bd=0)