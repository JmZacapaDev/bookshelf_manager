import argparse
import logging
from book_manager import BookManager

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    manager = BookManager()

    parser = argparse.ArgumentParser(description="Bookshelf Manager CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add book
    add_parser = subparsers.add_parser("add", help="Add a new book")
    add_parser.add_argument("isbn", type=str, help="ISBN of the book")
    add_parser.add_argument("title", type=str, help="Title of the book")
    add_parser.add_argument("author", type=str, help="Author of the book")

    # Search book
    search_parser = subparsers.add_parser("search", help="Search for a book")
    search_parser.add_argument("isbn", type=str, help="ISBN of the book")

    # Delete book
    delete_parser = subparsers.add_parser("delete", help="Delete a book")
    delete_parser.add_argument("isbn", type=str, help="ISBN of the book")

    # List books
    subparsers.add_parser("list", help="List all books")

    args = parser.parse_args()

    if args.command == "add":
        manager.add_book(args.isbn, args.title, args.author)
        logging.info(f"Book '{args.title}' added successfully.")

    elif args.command == "search":
        book = manager.get_book(args.isbn)
        if book:
            logging.info(f"Found Book: {book}")
        else:
            logging.warning("Book not found.")

    elif args.command == "delete":
        if manager.remove_book(args.isbn):
            logging.info("Book removed successfully.")
        else:
            logging.warning("Book not found.")

    elif args.command == "list":
        books = manager.get_books()
        if books:
            for book in books:
                logging.info(book)
        else:
            logging.info("No books found.")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()

