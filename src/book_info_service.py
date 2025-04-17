import requests
from abc import ABC, abstractmethod
from logger import get_logger


logger = get_logger(__name__)

class BookInfoService(ABC):
    """abstract base class for book info providers."""

    @abstractmethod
    def fetch_book_details(self, isbn: str) -> dict | None:
        """Fetches book details using the given ISBN."""
        pass

        try:
            response = requests.get(self.API_URL.format(isbn))
            response.raise_for_status()

            data = response.json()
            book_data = data.get(f"ISBN:{isbn}")

            if not book_data:
                logger.warning(f"No data found for ISBN: {isbn}")
                return None

            logger.info(f"Fetched book details for ISBN: {isbn}")
            return {
                "isbn": isbn,
                "title": book_data.get("title", "Unknown Title"),
                "author": book_data.get("authors", [{}])[0].get("name", "Unknown Author"),
                "publisher": book_data.get("publishers", [{}])[0].get("name", "Unknown Publisher"),
            }


        except request.RequestExceptions as e:
            logger.error(f"API request failed: {e}")
            return None


class OpenLibraryService(BookInfoService):
    API_URL_OPENLIB = "https://openlibrary.org/api/books?bibkeys=ISBN:{}&format=json&jscmd=data"

    def fetch_book_details(self, isbn: str) -> dict | None:

        try:
            response = requests.get(self.API_URL_OPENLIB.format(isbn))
            response.raise_for_status()
            data = response.json()
            book_data = data.get(f"ISBN:{isbn}")

            if not book_data:
                logger.warning(f"No Open Library data found for ISBN: {isbn}")
                return None

            logger.info(f"[OpenLibrary] Book found for ISBN: {isbn}")
            return {
                "isbn": isbn,
                "title": book_data.get("title", "Unknown Title"),
                "author": book_data.get("authors", [{}])[0].get("name", "Unknown Author"),
                "publisher": book_data.get("publishers", [{}])[0].get("name", "Unknown Publisher"),
            }

        except request.exceptions.RequestException as e:
            logger.error(f"Open Library API error: {e}")
            return None

class GoogleBooksService(BookInfoService):
    API_URL_GOOGLE = "https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"

    def fetch_book_details(self, isbn: str) -> dict | None:
        try:
            response = requests.get(self.API_URL.format(isbn))
            response.raise_for_status()
            data = response.json()
            items = data.get("items")

            if not items:
                logger.warning(f"No Google Books data found for ISBN: {isbn}")
                return None

            volume_info = items[0].get("volumeInfo", {})

            logger.info(f"[GoogleBooks] Book found for ISBN: {isbn}")
            return {
                "isbn": isbn,
                "title": volume_info.get("title", "Unknown Title"),
                "author": volume_info.get("authors", ["Unknown Author"])[0],
                "publisher": volume_info.get("publisher", "Unknown Publisher"),
            }

        except requests.exceptions.RequestException as e:
            logger.error(f"Google Books API error: {e}")
            return None


class ChainedBookInfoService(BookInfoService):
    """Tries multiple BookInfoServiceImplementations"""

    def __init__(self, services: list[BookInfoService]):
        self.services = services

    def fetch_book_details(self, isbn: str) -> dict | None:
        for service in self.services:
            result = service.fetch_book_details(isbn)
            if result:
                return result
        logger.warning(f"No book info found in any service for ISBN: {isbn}")
        return None
