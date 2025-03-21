from barcode_validator import BarcodeValidator
from barcode_processor import BarcodeProcessor
from barcode_scanner import KeyboardBarcodeScanner
from database_manager import DatabaseManager

'''
Scanner test
if __name__ == "__main__":
    validator = BarcodeValidator()
    scanner = KeyboardBarcodeScanner()
    processor = BarcodeProcessor(scanner, validator)

    barcode = processor.insert_barcode()
'''

if __name__ == "__main__":
    db = DatabaseManager()

    # Add a book
    db.add_book("9781234567890", "The Great Gatsby", "F. Scott Fitzgerald")

    # Retrieve a book
    book = db.get_book("9781234567890")
    print(book)  # ✅ Should print book details

    # Remove a book
    success = db.remove_book("9781234567890")
    print("Book removed" if success else "Book not found")

