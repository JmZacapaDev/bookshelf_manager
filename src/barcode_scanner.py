from abc import ABC, abstractmethod

class BarcodeScanner(ABC):
    "Defines an interface for barcode scanning functionality."

    @abstractmethod
    def scan_barcode(self) -> str:
        "Method to be implemented by any scanner system."
        pass

class KeyboardBarcodeScanner(BarcodeScanner):

    def scan_barcode(self) -> str:
        "Reads a barcode manuallyfrom user input."
        return input('Insert barcode: ').strip()
