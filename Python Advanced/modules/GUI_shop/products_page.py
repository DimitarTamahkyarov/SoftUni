from json import load, dump
from tkinter import Button

from PIL import ImageTk, Image

from helpers import clean_screen
from canvas import frame, root


def display_products():
    clean_screen()
    display_stock()


def display_stock():

    global products_info

    with open("db/product_data.json", "r") as stock:
        products_info = load(stock)

    x, y = 200, 20

    for product, info in products_info.items():
        item_img = ImageTk.PhotoImage(Image.open(info["image"]))
        images.append(item_img)

        frame.create_text(x, y, text=product, font=("Comic Sans MS", 15))
        frame.create_image(x, y + 120, image=item_img)

        if info["quantity"] > 0:
            color = "green"
            text = f"In stock: {info['quantity']}"

            item_btn = Button(
                root,
                text="Buy",
                bg="green",
                fg="white",
                font=15,
                command=lambda x=product: buy_product(x)
            )

            frame.create_window(400, y + 150, window=item_btn)
        else:
            color = "red"
            text = "Out of stock"

        frame.create_text(400, y + 100, text=text, fill=color, font=15)

        y += 280


def buy_product(product):
    products_info[product]["quantity"] -= 1

    with open("db/product_data.json", "w") as stock:
        dump(products_info, stock)

    display_products()


images = []
products_info = {}

