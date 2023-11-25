from flask import Flask
import random

app = Flask(__name__)

with open("quotes.txt", "r", encoding="UTF-8") as file:
    text = file.read()
    array_of_quotes = text.split("\n")
    random.shuffle(array_of_quotes)


@app.get("/random-quote")
def quotes_random_get():
    global array_of_quotes
    random_quote = random.choice(array_of_quotes)
    return f"<h1>{random_quote}</h1>"


app.run()
