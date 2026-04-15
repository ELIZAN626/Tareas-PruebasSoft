"""pruebas unitarias para el sistema de punto de venta"""

import unittest

from exercises5 import PointOfSale


class TestPointOfSale(unittest.TestCase):
    """clase de pruebas para el punto de venta"""

    def setUp(self):
        """configuracion inicial para cada prueba"""
        self.pos = PointOfSale()

    def test_scan_should_return_price_for_barcode_12345(self):
        """prueba precio de producto especifico"""
        result = self.pos.scan("12345")
        self.assertEqual(result, "$7.25")

    def test_scan_should_return_price_for_barcode_23456(self):
        """prueba precio de otro producto registrado"""
        result = self.pos.scan("23456")
        self.assertEqual(result, "$12.50")

    def test_scan_should_return_error_when_barcode_not_found(self):
        """prueba manejo de codigos inexistentes"""
        result = self.pos.scan("99999")
        self.assertEqual(result, "Error: barcode not found")

    def test_scan_should_return_error_when_barcode_is_empty(self):
        """prueba manejo de codigos vacios"""
        result = self.pos.scan("")
        self.assertEqual(result, "Error: empty barcode")

    def test_total_should_return_sum_of_scanned_product_prices(self):
        """prueba la suma total de productos validos"""
        self.pos.scan("12345")
        self.pos.scan("23456")

        result = self.pos.total()
        self.assertEqual(result, "$19.75")

    def test_total_should_ignore_invalid_scans(self):
        """prueba que el total ignore errores de escaneo"""
        self.pos.scan("12345")
        self.pos.scan("99999")
        self.pos.scan("")
        self.pos.scan("12345")

        result = self.pos.total()
        self.assertEqual(result, "$14.50")

    def test_total_should_return_zero_when_no_items_scanned(self):
        """prueba total en cero cuando no hay ventas"""
        result = self.pos.total()
        self.assertEqual(result, "$0.00")

    def test_scan_should_accumulate_multiple_identical_items(self):
        """prueba escaneo repetido del mismo producto"""
        self.pos.scan("12345")
        self.pos.scan("12345")
        self.pos.scan("12345")

        result = self.pos.total()
        self.assertEqual(result, "$21.75")

    def test_scan_should_handle_none_as_barcode(self):
        """prueba manejo de valor nulo"""
        result = self.pos.scan(None)
        self.assertEqual(result, "Error: empty barcode")

    def test_scan_should_ignore_whitespaces_in_barcode(self):
        """prueba limpieza de espacios en blanco"""
        result = self.pos.scan(" 12345 ")
        self.assertEqual(result, "$7.25")


if __name__ == "__main__":
    unittest.main()
