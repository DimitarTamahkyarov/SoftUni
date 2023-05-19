from json import load
from PIL import Image, ImageTk

from helpers import clean_screen


def display_products():
    clean_screen()


def displey_stock():
    with open("db/product_data.json", "r") as stock:
        products_info = load(stock)

    x, y = 100, 50

    for product, info in products_info.items():
        item_img = ImageTk.PhotoImage(Image.open(info["image"]))