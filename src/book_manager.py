from database_manager import DatabaseManager
from book_info_service import BookInfoService

class BookManager:
    """Handle Book CRUD operations"""

    def __init__(self):
        self.storage = DatabaseManager()

    def add_book(self, isbn: str, title: str, author: str):
        return self.storage.add_book(isbn, title, author)

    def find_book(self, isbn: str) -> dict | None:
        """Finds a book by ISBN."""
        return self.storage.get_book(isbn)

    def get_books(self) -> list[dict]:
        """Returns all stored books."""
        return self.storage.get_all_books()

    def remove_book(self, isbn: str) -> bool:
        """Removes a book by ISBN."""
        return self.storage.remove_book(isbn)

if __name__ == "__main__":
    manager = BookManager()

    book_data = {
        "isbn": "9781234567890",
        "title": "He Lives Again",
        "author": "Sahan Wiratunga"
    }

    manager.add_book(book_data)
    print(manager.get_books())
    print(manager.find_book("9781234567890"))
    print(manager.delete_book("9781234567890"))
