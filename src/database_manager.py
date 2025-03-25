import os
import sqlite3
from logger import get_logger

logger = get_logger(__name__)

DB_PATH = os.path.join("data", "books.db")

class DatabaseManager:
    """Handles SQLite database operations for book storage."""

    def __init__(self):
        """Ensures database connection and table creation."""
        self.conn = self.connect()
        self.create_table()

    def connect(self):
        """Connects to SQLite and ensures the 'data' directory exists."""
        os.makedirs("data", exist_ok=True)  # Ensure 'data/' exists
        return sqlite3.connect(DB_PATH)

    def create_table(self):
        """Creates the books table if it does not exist."""
        cursor = self.conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isbn TEXT UNIQUE NOT NULL,
            title TEXT NOT NULL,
            author TEXT NOT NULL
        );
        ''')
        self.conn.commit()

    def add_book(self, isbn: str, title: str, author: str):
        """Adds a book to the database."""
        cursor = self.conn.cursor()
        try:
            cursor.execute("INSERT INTO books (isbn, title, author) VALUES (?, ?, ?)",
                           (isbn, title, author))
            self.conn.commit()
            logger.info(f"Book added: {title} (isbn: {isbn})")
        except sqlite3.IntegrityError:
            logger.error(f"Duplicate entry: ISBN {isbn} already exists.")

    def get_book(self, isbn: str) -> dict | None:
        """Retrieves book details by ISBN."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM books WHERE isbn = ?", (isbn,))
        row = cursor.fetchone()
        if row:
            return {"id": row[0], "isbn": row[1], "title": row[2], "author": row[3]}
        return None

    def remove_book(self, isbn: str) -> bool:
        """Removes a book from the database by ISBN."""
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM books WHERE isbn = ?", (isbn,))
        self.conn.commit()
        return cursor.rowcount > 0  # Returns True if a book was deleted



