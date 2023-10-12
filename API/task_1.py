from io import BytesIO

import requests
from PIL import Image


def load_image(url):
    response = requests.get(url)
    picture = Image.open(BytesIO(response.content))
    picture.save("C:\\Users\\Lenovo\\Desktop\\images\\picture.png", "PNG")


load_image("https://apod.nasa.gov/apod/image/0503/marscliffs_express.jpg")
