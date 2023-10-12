import folium
import requests


def location(ip):
    # Протокол http вместо https потому, что я бедный!
    response = requests.get(f"http://ip-api.com/json/{ip}").json()
    m = folium.Map(location=[response["lat"], response["lon"]])
    folium.Marker(
        [response["lat"], response["lon"]],
        popup="South Korea",
    ).add_to(m)
    m.show_in_browser()


location("115.41.218.39")
