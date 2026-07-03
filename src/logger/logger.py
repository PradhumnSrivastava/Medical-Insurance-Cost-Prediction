import logging
import os
from datetime import datetime

# Create log file name with current date
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d')}.log"

# Create logs directory if it doesn't exist
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# Full path of log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(levelname)s - %(message)s",
    level=logging.INFO,
    filemode="a"
)