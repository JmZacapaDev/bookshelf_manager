import unittest
from src.barcode_validator import BarcodeValidator

class TestBarcodeValidator(unittest.TestCase):
    def setUp(self):
        """Create a validator instance before each test."""
        self.validator = BarcodeValidator()

    def test_valid_barcode(self):
        """Test barcodes that should be valid."""
        self.assertTrue(self.validator.validate_barcode("123456789012"))
        self.assertTrue(self.validator.validate_barcode("98765432109876"))

    def test_invalid_non_numeric(self):
        """Test barcodes containing letters or special characters."""
        self.assertFalse(self.validator.validate_barcode("abc123456789"))
        self.assertFalse(self.validator.validate_barcode("12@34567890!"))

    def test_invalid_too_short(self):
        """Test barcodes that are too short."""
        self.assertFalse(self.validator.validate_barcode("12345"))
        self.assertFalse(self.validator.validate_barcode("9876543"))

    def test_invalid_too_long(self):
        """Test barcodes that are too long."""
        self.assertFalse(self.validator.validate_barcode("1234567890123456"))
        self.assertFalse(self.validator.validate_barcode("987654321098765432"))

if __name__ == "__main__":
    unittest.main()

