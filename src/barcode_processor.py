class BarcodeProcessor:
    """Handles barcode input and processing."""

    def __init__(self, validator):
        self.validator = validator

    def insert_barcode(self) -> str:
        """Prompts the user for a barcode, validates it, and returns the valid barcode."""
        barcode = input("Insert barcode: ").strip()
        print("Validating your barcode...")

        if self.validator.validate_barcode(barcode):
            print("Barcode is valid:", barcode)
            return barcode

        print("Invalid barcode.")
        return None

