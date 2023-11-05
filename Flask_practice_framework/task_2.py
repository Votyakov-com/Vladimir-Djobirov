from flask import Flask, request

app = Flask(__name__)


@app.post("/api/convert_temperature")
def convert_temperature_post():
    data = request.json
    r = dict()
    r["fahrenheit"] = int(data["celsius"] * 1.8 + 32)
    return (r, 200, {"content-type": "application/json"})


app.run()
