import logging


# Logger config
logging.basicConfig(
    level=logging.INFO,  # Change to DEBUG for more details
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),  # Log to a file
        logging.StreamHandler()          # Log to console
    ]
)

def get_logger(name):
    """Returns a logger instance for a given module."""
    return logging.getLogger(name)
