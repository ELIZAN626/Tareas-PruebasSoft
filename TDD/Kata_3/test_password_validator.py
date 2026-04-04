"""casos de prueba para password validator"""

import unittest

from password_validator import validate_password


class TestPasswordValidator(unittest.TestCase):
    """casos de prueba para la funcion validate_password"""

    def test_valid_password(self):
        """valida que una constraseña valida regrese true y una lista vacia"""
        valid, errors = validate_password("Valid123!")
        self.assertTrue(valid)
        self.assertEqual(errors, [])

    def test_too_short(self):
        """valida que una contraseña tenga la longitud correcta de 8 caracteres y una cadena"""
        valid, errors = validate_password("Ab1!")
        self.assertFalse(valid)
        self.assertIn("Password must be at least 8 characters", errors)

    def test_less_than_two_numbers(self):
        """valida que la constraseña tenga 2 numeros"""
        valid, errors = validate_password("Validpass1!")
        self.assertFalse(valid)
        self.assertIn("The password must contain at least 2 numbers", errors)

    def test_no_capital_letter(self):
        """valida que la constraseña tenga 1 mayuscula"""
        valid, errors = validate_password("valid123!")
        self.assertFalse(valid)
        self.assertIn("password must contain at least one capital letter", errors)

    def test_no_special_character(self):
        """valida que la constraseña tenga un caracter especial valido"""
        valid, errors = validate_password("Valid1234")
        self.assertFalse(valid)
        self.assertIn("password must contain at least one special character", errors)

    def test_multiple_errors(self):
        """valida que las validaciones esten completas y no falte ninguna"""
        valid, errors = validate_password("short")
        self.assertFalse(valid)
        self.assertEqual(len(errors), 4)  # length, numbers, capital, special
        # verificamos que los mensajes esperados estén presentes
        expected = [
            "Password must be at least 8 characters",
            "The password must contain at least 2 numbers",
            "password must contain at least one capital letter",
            "password must contain at least one special character",
        ]
        for msg in expected:
            self.assertIn(msg, errors)


if __name__ == "__main__":
    unittest.main()
