import requests


def request_status(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("Запрос успешно выполнен!")
    else:
        print("Произошла ошибка при выполнении запроса!")
    print('Код состояния HTTP-ответа:', response.status_code)


