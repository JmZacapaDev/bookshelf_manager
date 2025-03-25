from barcode_scanner   import BarcodeScanner
from barcode_validator import BarcodeValidator
from logger            import get_logger

logger = get_logger(__name__)

class BarcodeProcessor:
    """Handles barcode scanning and validation."""

    def __init__(self, scanner: BarcodeScanner, validator: BarcodeValidator):
        self.scanner = scanner
        self.validator = validator

    def insert_barcode(self) -> str:
        """Scans and validates a barcode."""
        barcode = self.scanner.scan_barcode()

        if not barcode:
            logger.warning("Empty barcode input detected.")
            return None

        if not self.validator.validate_barcode(barcode):
            logger.error(f"Invalid barcode entered: {barcode}")
            return None

        logger.info(f"Valid barcode processed: {barcode}")
        return barcode

