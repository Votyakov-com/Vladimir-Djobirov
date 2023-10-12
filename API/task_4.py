import black
import requests


def weather_in_place(city):
    response = requests.get(
        f"https://api.weatherapi.com/v1/current.json"
        f"?key=698615f8032c4457adb172050230410&q={city}&aqi=yes"
    )
    formatted_code = black.format_file_contents(
        response.text, fast=False, mode=black.FileMode()
    )
    print(formatted_code)


weather_in_place("Moscow")
