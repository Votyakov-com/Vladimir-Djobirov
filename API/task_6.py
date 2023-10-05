import numpy as np
import requests
from matplotlib import pyplot as plt


def weather_forecast(city, days):
    api_key = "698615f8032c4457adb172050230410"
    response = requests.get(
        f"https://api.weatherapi.com/v1/forecast.json"
        f"?key={api_key}&q={city}&days={days}&aqi=yes&alerts=yes"
    )

    data = response.json()

    list_of_dates = [i["date"] for i in data["forecast"]["forecastday"]]
    list_of_temperatures = [
        i["day"]["avgtemp_c"] for i in data["forecast"]["forecastday"]
    ]

    array_of_temperatures = np.array(list_of_temperatures)
    array_of_dates = np.array(list_of_dates)

    plt.figure(figsize=(10, 5))
    plt.plot(array_of_dates, array_of_temperatures)
    plt.title(f"График прогноза погоды на неделю в городе {city}", size=16)
    plt.xlabel("Даты", size=12)
    plt.ylabel("Температура (в градусах Цельсия)", size=12)
    plt.grid()
    plt.show()

    print("График успешно создан!")


# Example:
weather_forecast("Ekaterinburg", 7)
