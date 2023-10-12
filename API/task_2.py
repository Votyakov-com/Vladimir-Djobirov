import requests


def check(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("Сайт находится в открытом доступе!")
    else:
        print("В данный момент сайт недоступен!")
