import requests
from logger import get_logger

logger = get_logger(__name__)

class BookInfoService:
    """Fetches book details from an external API (Open Library)."""

    API_URL = "https://openlibrary.org/api/books?bibkeys=ISBN:{}&format=json&jscmd=data"

    def fetch_book_details(self, isbn: str) -> dict | None:
        """Fetches book details using the given ISBN."""
        response = requests.get(self.API_URL.format(isbn))

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

