from json import load
from PIL import ImageTk, Image

from helpers import clean_screen
from canvas import frame


def display_products():
    clean_screen()
    display_stock()


def display_stock():
    with open("db/product_data.json", "r") as stock:
        products_info = load(stock)

    x, y = 250, 20

    for product, info in products_info.items():
        item_img = ImageTk.PhotoImage(Image.open(info["image"]))
        images.append(item_img)

        frame.create_text(x, y, text=product, font=("Comic Sans MS", 15))
        frame.create_image(x, y + 120, image=item_img,)

        y += 280


images = []