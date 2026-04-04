"""Modulo para el kata FizzBuzz."""


def fizzbuzz(n):
    """Devuelve Fizz, Buzz o FizzBuzz segun reglas."""
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)
