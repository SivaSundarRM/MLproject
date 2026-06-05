import logging
import os
import datetime

LOG_FILE = f"logs/{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs",LOG_FILE)
os.makedirs(os.path.dirname(logs_path), exist_ok=True)


LOG_FILE_PATH = os.path.join(os.getcwd(), "logs", LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


if __name__ == "__main__":
    logging.info("This is an info message.")
    logging.warning("This is a warning message.")
    logging.error("This is an error message.")