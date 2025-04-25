import csv
import json
from database_manager import DatabaseManager
from book_info_service import BookInfoService
from logger import get_logger

logger = get_logger(__name__)


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

    def export_to_csv(self, file_path: str) -> None:
        """Save all books info in a CSV File"""
        books = self.storage.get_all_books()

        if not books:
            logger.error(f"No books to export.")

        with open(file_path, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["id", "isbn", "title", "author"])
            writer.writeheader()
            writer.writerows(books)
            logger.info(f"Books info saved in CSV file at: {file_path}")


    def export_to_json(self, file_path: str) -> None:
        """Save all books info in a json File"""
        books = self.storage.get_all_books()

        if not books:
            logger.error(f"No books to export.")
            return


        try:
            with open(file_path, "w", encoding="utf-8") as jsonf:
                json.dump(books,jsonf,ensure_ascii = False, indent=4)
            logger.info(f"books info saved to Json file at {file_path}")

        except Exception as e:
            logger.error(f"Failed to export books to JSON {e}")

if __name__ == "__main__":
    manager = BookManager()

    book_data = {
        "isbn": "9781234567890",
        "title": "He Lives Again",
        "author": "Sahan Wiratunga"
    }

    manager.add_book(book_data["isbn"], book_data["title"], book_data["author"])
    print(manager.get_books())
    print(manager.find_book("9781234567890"))
    manager.export_to_json("my_books.json")
    print(manager.remove_book("9781234567890"))
