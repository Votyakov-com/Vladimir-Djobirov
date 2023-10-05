import black
import requests


def converter_currency(start_currency, required_currency=""):
    response = requests.get(
        f"https://api.freecurrencyapi.com/v1/"
        f"latest?apikey=fca_live_OOl9PaK1YExXS"
        f"h82TanLSe6Jq3260WJjSOoe1RVI&currencies="
        f"{required_currency}&base_currency={start_currency}"
    )

    formatted_code = black.format_file_contents(
        response.text, fast=False, mode=black.FileMode()
    )
    print(formatted_code)
