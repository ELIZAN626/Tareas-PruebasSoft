# -*- coding: utf-8 -*-

"""
Test cases for mockup_exercises.py
"""

import subprocess
import time
import unittest
from unittest.mock import Mock, mock_open, patch

import mockup_exercises
import requests


class TestMockupExercises(unittest.TestCase):
    """funciones de prueba para mockup_exercises.py"""

    # Pruebas para fetch_data_from_api

    @patch("requests.get")
    def test_fetch_data_from_api_success(self, mock_get):
        """Prueba que fetch_data_from_api retorna datos JSON correctamente."""

        # Configurar el mock
        mock_response = Mock()
        mock_response.json.return_value = {"key": "value"}
        mock_get.return_value = mock_response

        # Ejecutar la funcion
        result = mockup_exercises.fetch_data_from_api("http://test.com/api")

        # Verificar resultados
        mock_get.assert_called_once_with("http://test.com/api", timeout=10)
        self.assertEqual(result, {"key": "value"})

    @patch("requests.get")
    def test_fetch_data_from_api_timeout(self, mock_get):
        """Prueba que fetch_data_from_api maneja timeout correctamente."""

        # Simulamos un timeout
        mock_get.side_effect = requests.exceptions.Timeout()

        # Verificar que lanza excepcion
        with self.assertRaises(requests.exceptions.Timeout):
            mockup_exercises.fetch_data_from_api("http://test.com/api")

    # Pruebas para read_data_from_file
    @patch("builtins.open", new_callable=mock_open, read_data="contenido de prueba")
    def test_read_data_from_file_success(self, mock_file):
        """Prueba que read_data_from_file lee archivos correctamente."""
        result = mockup_exercises.read_data_from_file("test.txt")

        mock_file.assert_called_once_with("test.txt", encoding="utf-8")
        self.assertEqual(result, "contenido de prueba")

    @patch("builtins.open")
    def test_read_data_from_file_not_found(self, mock_file):
        """Prueba que read_data_from_file maneja archivo no encontrado."""
        mock_file.side_effect = FileNotFoundError()

        with self.assertRaises(FileNotFoundError):
            mockup_exercises.read_data_from_file("no_existe.txt")

    # Pruebas para execute_command
    @patch("subprocess.run")
    def test_execute_command_success(self, mock_run):
        """Prueba que execute_command ejecuta comandos correctamente."""
        # Configurar mock
        mock_result = Mock()
        mock_result.stdout = "comando ejecutado"
        mock_run.return_value = mock_result

        result = mockup_exercises.execute_command(["ls", "-la"])

        mock_run.assert_called_once_with(
            ["ls", "-la"], capture_output=True, check=False, text=True
        )
        self.assertEqual(result, "comando ejecutado")

    @patch("subprocess.run")
    def test_execute_command_error(self, mock_run):
        """Prueba que execute_command maneja errores del subprocess."""

        mock_run.side_effect = subprocess.CalledProcessError(1, "cmd")

        with self.assertRaises(subprocess.CalledProcessError):
            mockup_exercises.execute_command(["comando", "invalido"])

    # Pruebas para perform_action_based_on_time
    @patch("time.time")
    def test_perform_action_based_on_time_less_than_10(self, mock_time):
        """Prueba que retorna Action A cuando time < 10."""

        mock_time.return_value = 5

        result = mockup_exercises.perform_action_based_on_time()

        self.assertEqual(result, "Action A")

    @patch("time.time")
    def test_perform_action_based_on_time_greater_equal_10(self, mock_time):
        """Prueba que retorna Action B cuando time >= 10."""

        mock_time.return_value = 10

        result = mockup_exercises.perform_action_based_on_time()

        self.assertEqual(result, "Action B")

    @patch("time.time")
    def test_perform_action_based_on_time_more_than_10(self, mock_time):
        """Prueba que retorna Action B cuando time > 10."""

        mock_time.return_value = 15

        result = mockup_exercises.perform_action_based_on_time()

        self.assertEqual(result, "Action B")

    # ? CASOS ADICIONALES para verificar errores

    def test_perform_action_never_returns_a(self):
        """Demuestra que Action A NUNCA ocurre en ejecucion real."""

        resultados = []
        for _ in range(30):
            resultados.append(mockup_exercises.perform_action_based_on_time())
            time.sleep(0.1)

        # Esta prueba FALLARA porque la funcion solo retorna "Action B"
        # Esto revela el error de diseño en la funcion
        self.assertIn(
            "Action A",
            resultados,
            "ERROR: Action A nunca ocurre - la funcion esta mal diseñada",
        )

    @patch("requests.get")
    def test_fetch_api_no_http_error_handling(self, mock_get):
        """Revela que la funcion no maneja errores HTTP como 404."""

        mock_response = Mock()
        mock_response.json.return_value = {"error": "not found"}
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(
            "404 Error"
        )
        mock_get.return_value = mock_response

        # La funcion deberia lanzar excepcion pero no lo hace
        resultado = mockup_exercises.fetch_data_from_api("http://test.com/api")

        # la funcion deberia haber fallado
        # Esta asercion PASARA pero revela el error porque deberia haber fallado antes
        self.assertEqual(
            resultado,
            {"error": "not found"},
            "ERROR: La funcion deberia haber lanzado HTTPError",
        )

    @patch("requests.get")
    def test_fetch_api_no_json_error_handling(self, mock_get):
        """Revela que la funcion no maneja respuestas que no son JSON."""

        mock_response = Mock()
        mock_response.json.side_effect = ValueError("Invalid JSON")
        mock_get.return_value = mock_response

        # La funcion lanzara ValueError pero deberia manejarlo
        with self.assertRaises(ValueError) as context:
            mockup_exercises.fetch_data_from_api("http://test.com/api")

        # Esto debe revelar que la funcion no tiene manejo de errores para JSON invalido
        self.assertIn(
            "Invalid JSON",
            str(context.exception),
            "ERROR: La funcion deberia manejar JSON invalido",
        )

    def test_file_error_handling_is_redundant(self):
        """Demuestra que el try/except para FileNotFoundError es redundante."""

        with patch("builtins.open") as mock_file:
            mock_file.side_effect = FileNotFoundError("Archivo no encontrado")

            # La excepcion se propaga igual que sin try/except
            with self.assertRaises(FileNotFoundError) as context:
                mockup_exercises.read_data_from_file("no_existe.txt")

            # Verificar que el mensaje de error se mantiene
            self.assertIn(
                "Archivo no encontrado",
                str(context.exception),
                "ERROR: El try/except no agrega valor - es redundante",
            )

    def test_command_error_handling_is_redundant(self):
        """Demuestra que el try/except para CalledProcessError es redundante."""

        with patch("subprocess.run") as mock_run:
            mock_run.side_effect = subprocess.CalledProcessError(
                1, "cmd", output="Error"
            )

            # La excepcion se propaga igual que sin try/except
            with self.assertRaises(subprocess.CalledProcessError) as context:
                mockup_exercises.execute_command(["comando", "invalido"])

            # Verificar que el codigo de error se mantiene
            self.assertEqual(
                context.exception.returncode,
                1,
                "ERROR: El try/except no agrega valor - es redundante",
            )


if __name__ == "__main__":
    unittest.main()
