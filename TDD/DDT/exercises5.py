"""modulo para sistema de punto de venta"""


class PointOfSale:
    """clase que maneja el escaneo y total de productos"""

    def __init__(self):
        self.products = {"12345": 7.25, "23456": 12.50}
        self.scanned_prices = []

    def scan(self, barcode):
        """escanea un codigo de barras y devuelve el precio"""

        if barcode is not None:
            barcode = barcode.strip()

        if not barcode:
            return "Error: empty barcode"

        if barcode not in self.products:
            return "Error: barcode not found"

        price = self.products[barcode]
        self.scanned_prices.append(price)
        return f"${price:.2f}"

    def total(self):
        """calcula el total acumulado de los productos"""
        total_sum = sum(self.scanned_prices)
        return f"${total_sum:.2f}"
