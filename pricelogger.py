import logging

formatter = logging.Formatter(
    '[%(asctime)s] %(name)s %(levelname)s %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S %Z'
)

price_logger = logging.getLogger('price')

file_handler = logging.FileHandler('prices.log')
file_handler.setFormatter(formatter)
price_logger.addHandler(file_handler)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
price_logger.addHandler(stream_handler)

price_logger.setLevel(logging.INFO)

def log(msg):
    return price_logger.info(msg)

