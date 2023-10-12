from io import BytesIO

import requests
from PIL import Image


def nasa_picture(date):
    api_key = "uWmbBcNBVWDlffolNQkQ0JMcPn1Ojg0bBSRqrqad"
    response_first = requests.get(
        f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date}"
    )

    data = response_first.json()
    url_picture = data["url"]
    response_second = requests.get(url_picture)
    picture = Image.open(BytesIO(response_second.content))
    # Перед использованием нужно создать папку на рабочем столе: images
    picture.save("C:\\Users\\Lenovo\\Desktop\\images\\picture.gif", "GIF")


# Example:
nasa_picture("2022-07-07")
