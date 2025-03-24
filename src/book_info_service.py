import requests

class BookInfoService:
    """Fetches book details from an external API (Open Library)."""

    API_URL = "https://openlibrary.org/api/books?bibkeys=ISBN:{}&format=json&jscmd=data"

    def fetch_book_details(self, isbn: str) -> dict | None:
        """Fetches book details using the given ISBN."""
        response = requests.get(self.API_URL.format(isbn))

        if response.status_code != 200:
            print("Error: Unable to fetch book details.")
            return None

        data = response.json()
        book_data = data.get(f"ISBN:{isbn}")

        if not book_data:
            print("Error: No book data found for this ISBN.")
            return None

        return {
            "isbn": isbn,
            "title": book_data.get("title", "Unknown Title"),
            "author": book_data.get("authors", [{}])[0].get("name", "Unknown Author"),
            "publisher": book_data.get("publishers", [{}])[0].get("name", "Unknown Publisher"),
        }
