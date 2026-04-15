"""pruebas para la funcionalidad de busqueda de ciudades"""

import json
import os
import unittest

from exercises4 import search_cities


class TestSearchCities(unittest.TestCase):
    """clase de pruebas para verificar el filtro de ciudades"""

    @classmethod
    def setUpClass(cls):
        file_path = os.path.join(os.path.dirname(__file__), "cities.json")
        with open(file_path, "r", encoding="utf-8") as f:
            cls.all_cities = json.load(f)["cities"]

    def test_should_return_no_results_if_search_text_is_fewer_than_2_chars(self):
        """verifica que no retorne nada con menos de dos caracteres"""
        self.assertEqual(search_cities("a"), [])
        self.assertEqual(search_cities(""), [])

    def test_should_return_cities_starting_with_search_text(self):
        """verifica que encuentre ciudades por su inicio"""
        self.assertEqual(search_cities("Va"), ["Valencia", "Vancouver"])
        self.assertEqual(search_cities("Pa"), ["Paris"])

    def test_should_be_case_insensitive(self):
        """verifica que no importe si es mayuscula o minuscula"""
        self.assertEqual(search_cities("va"), ["Valencia", "Vancouver"])
        self.assertEqual(search_cities("PARIS"), ["Paris"])
        self.assertEqual(search_cities("nEw"), ["New York City"])

    def test_should_return_cities_when_search_text_is_part_of_name(self):
        """verifica coincidencias en cualquier parte del nombre"""
        self.assertEqual(search_cities("ape"), ["Budapest"])
        self.assertEqual(search_cities("dam"), ["Rotterdam", "Amsterdam"])

    def test_should_return_all_cities_when_asterisk_is_passed(self):
        """verifica que el asterisco retorne la lista completa"""
        self.assertEqual(search_cities("*"), self.all_cities)


if __name__ == "__main__":
    unittest.main()
