from rembg import remove
from PIL import Image

image_input = Image.open("./FB_IMG_1528005820319.jpg")
output = remove(image_input)
output.save("./output.jpg")