"""modulo que implementa validador de contraseñas"""

import re


def validate_password(password):
    """validamos constraseñas segun distintas reglas"""
    errors = []

    if len(password) < 8:
        errors.append("Password must be at least 8 characters")

    if len(re.findall(r"\d", password)) < 2:
        errors.append("The password must contain at least 2 numbers")

    if not re.search(r"[A-Z]", password):
        errors.append("password must contain at least one capital letter")

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        errors.append("password must contain at least one special character")

    is_valid = len(errors) == 0
    return is_valid, errors
