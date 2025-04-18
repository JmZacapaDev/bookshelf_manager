from barcode_validator import BarcodeValidator
from barcode_processor import BarcodeProcessor
from barcode_scanner   import KeyboardBarcodeScanner
from database_manager  import DatabaseManager
from book_info_service import (
        ChainedBookInfoService,
        OpenLibraryService,
        GoogleBooksService
        )

def main():
    book_service = ChainedBookInfoService([
        OpenLibraryService(),
        GoogleBooksService()
    ])
    storage = DatabaseManager()

    # Sample ISBN
    isbn = "9781234567890"

    book_data = book_service.fetch_book_details(isbn)

    if book_data:
        print(f'Fetched Book: {book_data}')

        storage.add_book(book_data["isbn"], book_data["title"], book_data["author"])

        book = storage.get_book(book_data["isbn"])
        print(f'Stored book:{book}')

        success = storage.remove_book(book_data["isbn"])
        print("Book removed" if success else "Book not found")


if __name__ == "__main__":
    main()
