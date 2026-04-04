"""Modulo para el kata string calculator"""

import re


def add(numbers):
    """funcion que suma numeros separados por medio de delimitadores en una cadena"""
    if not numbers:
        return 0

    delimiter = ",|\n"
    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        delimiter = re.escape(parts[0][2:])
        numbers = parts[1]

    num_list = re.split(delimiter, numbers)

    if num_list and num_list[-1] == "":
        raise ValueError("Trailing separator not allowed")

    negatives = [int(n) for n in num_list if int(n) < 0]
    if negatives:
        raise ValueError(
            f"Negative number(s) not allowed: {','.join(map(str, negatives))}"
        )

    total = sum(int(n) for n in num_list if int(n) <= 1000)
    return total
