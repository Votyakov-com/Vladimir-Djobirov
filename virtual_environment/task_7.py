from os import getenv

from dotenv import load_dotenv

load_dotenv("C:\\Users\\Lenovo\\PycharmProjects\\pythonProject\\file.env")
print(getenv('API_KEY'))
