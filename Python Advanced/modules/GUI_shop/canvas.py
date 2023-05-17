from tkinter import *


def create_root():
    root = Tk()
    root.resizable(False, False)
    root.geometry("500x600")
    root.title("GUI Product Shop")

    return root


def create_frame():
    frame = Canvas(root, width=500, height=600)
    frame.grid(row=0, column=0)

    return frame


root = create_root()
frame = create_frame()


