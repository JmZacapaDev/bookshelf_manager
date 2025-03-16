from barcode_validator import BarcodeValidator
from barcode_processor import BarcodeProcessor
from barcode_scanner import KeyboardBarcodeScanner


if __name__ == "__main__":
    validator = BarcodeValidator()
    scanner = KeyboardBarcodeScanner()
    processor = BarcodeProcessor(scanner, validator)

    barcode = processor.insert_barcode()
