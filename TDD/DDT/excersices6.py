"""modulo para gestionar transacciones bancarias"""

from datetime import date

# from unittest.mock import call, patch


class Account:
    """clase que representa una cuenta de banco"""

    def __init__(self):
        # Internal list to store transactions as (date_str, amount, balance)
        self._transactions = []
        self._balance = 0

    def deposit(self, amount):
        """registra un deposito en la cuenta"""
        # Requirement 1: Deposit into Account
        self._balance += amount
        today = date.today().strftime("%d/%m/%Y")
        self._transactions.append((today, amount, self._balance))

    def withdraw(self, amount):
        """registra un retiro de la cuenta"""
        # Requirement 2: Withdraw from an Account
        self._balance -= amount
        today = date.today().strftime("%d/%m/%Y")
        self._transactions.append((today, -amount, self._balance))

    def print_statement(self):
        """imprime el estado de cuenta en consola"""
        # Requirement 3: Print the Account statement to the console
        # Transactions are printed in reverse order (most recent first)
        print("DATE       | AMOUNT  | BALANCE")
        for transaction_date, amount, balance in reversed(self._transactions):
            print(f"{transaction_date} | {amount:.2f} | {balance:.2f}")
