# logger.py
# Configure logging to write to a file
import logging

logging.basicConfig(
    filename='app.log',
    filemode='w',  # 'w' for overwrite, 'a' for append
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
