class BarcodeValidator:
    """Handles barcode validation logic."""

    def validate_barcode(self, barcode: str) -> bool:
        """Validates the barcode by checking its format and length."""
        if not self._is_numeric(barcode):
            return False

        if not self._is_valid_length(barcode):
            return False

        return True

    def _is_numeric(self, barcode: str) -> bool:
        """Checks if the barcode consists only of digits."""
        return barcode.isdigit()

    def _is_valid_length(self, barcode: str) -> bool:
        """Checks if the barcode length is between 11 and 14 digits."""
        return 11 <= len(barcode) <= 14
