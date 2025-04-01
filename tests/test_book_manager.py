import unittest
from src.book_manager import BookManager
from src.database_manager import DatabaseManager

class TestBookManager(unittest.TestCase):

    def setUp(self):
        """Set up a fresh database for each test."""
        self.db = DatabaseManager(':memory:')  # Use in-memory DB for tests
        self.manager = BookManager(self.db)
        self.db.create_schema()

    def tearDown(self):
        """Close the database after each test."""
        self.db.close()

    def test_add_book(self):
        """Test adding a book."""
        self.manager.add_book("9781234567890", "He Lives Again", "Sahan Wiratunga")
        books = self.manager.get_all_books()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]['isbn'], "9781234567890")

    def test_get_all_books_empty(self):
        """Test retrieving books when database is empty."""
        books = self.manager.get_all_books()
        self.assertEqual(len(books), 0)

    def test_remove_book(self):
        """Test removing a book."""
        self.manager.add_book("9781234567890", "He Lives Again", "Sahan Wiratunga")
        self.manager.remove_book("9781234567890")
        books = self.manager.get_all_books()
        self.assertEqual(len(books), 0)

    def test_search_book(self):
        """Test searching for a book by ISBN."""
        self.manager.add_book("9781234567890", "He Lives Again", "Sahan Wiratunga")
        book = self.manager.get_book("9781234567890")
        self.assertIsNotNone(book)
        self.assertEqual(book['title'], "He Lives Again")

    def test_list_books(self):
        """Test listing all books."""
        self.manager.add_book("9781234567890", "He Lives Again", "Sahan Wiratunga")
        self.manager.add_book("9780987654321", "Another Book", "Jane Doe")
        books = self.manager.get_all_books()
        self.assertEqual(len(books), 2)

if __name__ == '__main__':
    unittest.main()

