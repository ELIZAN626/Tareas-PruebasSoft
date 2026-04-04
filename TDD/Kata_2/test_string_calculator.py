"""Pruebas unitarias para el modulo de string calculator"""

import unittest

from string_calculator import add


class TestStringCalculator(unittest.TestCase):
    """casos de prueba para la funcion add."""

    def test_empty_string_returns_zero(self):
        """revisa que un string vacio retorne 0"""
        self.assertEqual(add(""), 0)

    def test_one_number_returns_itself(self):
        """revisa que un solo numero regrese el mismo valor"""
        self.assertEqual(add("1"), 1)

    def test_two_numbers_comma_separated(self):
        """checa que la suma de dos numeros sean separados por una coma"""
        self.assertEqual(add("1,2"), 3)

    def test_unknown_amount_of_numbers(self):
        """checa una suma de una cantidad variable de numeros"""
        self.assertEqual(add("1,2,3,4"), 10)

    def test_newline_as_separator(self):
        """checa que el salto de linea sea un separador"""
        self.assertEqual(add("1\n2,3"), 6)

    def test_trailing_separator_raises_error(self):
        """revisa que un separador al final lance una excepcion"""
        with self.assertRaises(ValueError):
            add("1,2,")

    def test_custom_delimiter(self):
        """hace que los delimitadores personalziados si funcionen"""
        self.assertEqual(add("//;\n1;2"), 3)

    def test_negative_numbers_not_allowed(self):
        """checa que los numeros negativos lancen una excepcion"""
        with self.assertRaises(ValueError) as ctx:
            add("1,-2,3")
        self.assertEqual(str(ctx.exception), "Negative number(s) not allowed: -2")

    def test_ignore_numbers_greater_than_1000(self):
        """verifica que numeros mayores a 1000 se pasen de largo"""
        self.assertEqual(add("2,1001"), 2)


if __name__ == "__main__":
    unittest.main()
