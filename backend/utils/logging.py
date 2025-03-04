import logging

# all the logging should be done like this...
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_info(message: str):
    logging.info(message)

def log_error(message: str):
    logging.error(message)