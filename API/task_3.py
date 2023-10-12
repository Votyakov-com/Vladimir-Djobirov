import requests
from bs4 import BeautifulSoup


def parse(url):
    with open("anime_list.txt", "w") as file:
        response = requests.get(url)

        soup = BeautifulSoup(response.text, "lxml")

        anime_text = soup.find_all("blockquote", class_="wp-block-quote")
        clear_anime_text = [anime.text for anime in anime_text]
        for i in range(len(clear_anime_text)):
            file.write(f"{i + 1}) {clear_anime_text[i]}\n \n")
        print(f"Цитаты успешно записаны в {file.name}")


def main():
    parse("https://quotebat.com/120-luchshih-citat-iz-anime-vseh-vremen/")


if __name__ == "__main__":
    main()
