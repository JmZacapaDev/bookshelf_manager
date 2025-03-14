from barcode_validator import BarcodeValidator
from barcode_processor import BarcodeProcessor

if __name__ == "__main__":
    validator = BarcodeValidator()
    processor = BarcodeProcessor(validator)

    barcode = processor.insert_barcode()
