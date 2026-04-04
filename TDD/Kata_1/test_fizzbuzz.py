"""pruebas FizzBuzz."""

import unittest

from fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    """casos de prueba para el kata FizzBuzz"""

    def test_return_number_as_string(self):
        """checamos que los numeros se regresen como cadena"""
        self.assertEqual(fizzbuzz(1), "1")
        self.assertEqual(fizzbuzz(2), "2")

    def test_multiple_of_three_returns_fizz(self):
        """checamos que multiplos de 3 regresen fizz"""
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(6), "Fizz")

    def test_multiple_of_five_returns_buzz(self):
        """verificamos que multiplos de 5 regresen buzz"""
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(10), "Buzz")

    def test_multiple_of_three_and_five_returns_fizzbuzz(self):
        """multiplos de 3 y 5 regresan fizzbuzz"""
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz(30), "FizzBuzz")


if __name__ == "__main__":
    unittest.main()
