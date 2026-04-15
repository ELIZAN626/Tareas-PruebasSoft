"""modulo para busqueda de ciudades en archivos json"""

import json
import os


def search_cities(search_text):
    """busca ciudades segun el texto ingresado"""
    file_path = os.path.join(os.path.dirname(__file__), "cities.json")
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        cities = data["cities"]

    if search_text == "*":
        return cities

    if len(search_text) < 2:
        return []
    search_lower = search_text.lower()

    cities_found = []

    for city in cities:
        city_lower = city.lower()

        if search_lower in city_lower:
            cities_found.append(city)

    return cities_found
