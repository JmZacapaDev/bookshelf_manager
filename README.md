# bookshelf_manager
# Library Inventory Management Project

This project is an inventory management application for private libraries. The goal is to register, organize, and manage books efficiently, allowing users to obtain book information (title, author, publisher, etc.) using the barcode. The project is built in **Python** and stores data in a local **SQLite** database.

## Features

- Manually register books with basic information (title, author, publisher, etc.).
- Scan barcodes to add books automatically.
- Store books in an SQLite database.
- Automatically retrieve book data from an API (to be implemented in future sprints).

## Technologies

- **Python**: Main programming language.
- **SQLite**: Local database.
- **Tkinter** or **PyQt** (depending on the chosen GUI): For the user interface.
- **Pillow**: For handling images, such as book covers.
- **Pyzbar** or **zxing**: For reading barcodes (future).
- **Open Library API** or **Google Books API**: For automatically retrieving book data (future).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/JmZacapaDev/bookshelf_manager.git
