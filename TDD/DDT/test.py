"""pruebas unitarias para la clase account"""

import unittest
from io import StringIO
from unittest.mock import patch

from excersices6 import Account


class TestAccount(unittest.TestCase):
    """clase de pruebas para verificar movimientos bancarios"""

    @classmethod
    def setUpClass(cls):
        """configuracion inicial de datos para las pruebas"""
        cls.test_data = [
            {
                "description": "single deposit updates balance",
                "actions": [("deposit", 1000)],
                "expected_balance": 1000,
            },
            {
                "description": "multiple deposits accumulate balance",
                "actions": [("deposit", 1000), ("deposit", 500)],
                "expected_balance": 1500,
            },
            {
                "description": "withdraw reduces balance",
                "actions": [("deposit", 1000), ("withdraw", 100)],
                "expected_balance": 900,
            },
            {
                "description": "multiple withdrawals reduce balance correctly",
                "actions": [("deposit", 1000), ("withdraw", 200), ("withdraw", 300)],
                "expected_balance": 500,
            },
            {
                "description": "print_statement outputs header",
                "actions": [],
                "expected_in_output": "DATE       | AMOUNT  | BALANCE",
            },
            {
                "description": "print_statement shows transactions in reverse order",
                "actions": [("deposit", 1000), ("withdraw", 100), ("deposit", 500)],
                "expected_lines_contain": ["500.00", "-100.00", "1000.00"],
            },
            {
                "description": "deposit amount is positive in statement",
                "actions": [("deposit", 1000)],
                "expected_in_output": "1000.00",
            },
            {
                "description": "withdrawal amount is negative in statement",
                "actions": [("deposit", 1000), ("withdraw", 100)],
                "expected_in_output": "-100.00",
            },
            {
                "description": "balance after deposit and withdraw matches kata example",
                "actions": [("deposit", 1000), ("deposit", 500), ("withdraw", 100)],
                "expected_balance": 1400,
            },
        ]

    def _get_printed_output(self, account):
        """ayuda a capturar la salida de print_statement"""
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            account.print_statement()
            return mock_stdout.getvalue()

    def _apply_actions(self, account, actions):
        """aplica una lista de acciones de deposito o retiro"""
        for method, amount in actions:
            getattr(account, method)(amount)

    def test_account(self):
        """prueba la clase account con varios escenarios de transacciones"""
        for x in self.test_data:
            with self.subTest(description=x["description"]):
                account = Account()
                self._apply_actions(account, x["actions"])

                if "expected_balance" in x:
                    # pylint: disable=protected-access
                    self.assertEqual(account._balance, x["expected_balance"])

                if "expected_in_output" in x:
                    output = self._get_printed_output(account)
                    self.assertIn(x["expected_in_output"], output)

                if "expected_lines_contain" in x:
                    output = self._get_printed_output(account)
                    lines = output.strip().split("\n")[1:]
                    for i, expected_value in enumerate(x["expected_lines_contain"]):
                        self.assertIn(expected_value, lines[i])

    def test_print_statement_full_scenario(self):
        """prueba el escenario completo del ejemplo de la kata"""
        account = Account()

        with patch("excersices6.date") as mock_date:
            mock_date.today.return_value.strftime.side_effect = [
                "01/04/2014",
                "02/04/2014",
                "10/04/2014",
            ]
            account.deposit(1000)
            account.withdraw(100)
            account.deposit(500)

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            account.print_statement()
            output = mock_stdout.getvalue()

        lines = output.strip().split("\n")

        self.assertEqual(lines[0], "DATE       | AMOUNT  | BALANCE")
        self.assertIn("10/04/2014", lines[1])
        self.assertIn("02/04/2014", lines[2])
        self.assertIn("01/04/2014", lines[3])


if __name__ == "__main__":
    unittest.main()
