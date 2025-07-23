import logging
from logging.handlers import RotatingFileHandler

#Rotating File Handler
handler = RotatingFileHandler('rotate.log', maxBytes=1000, backupCount=3)
logging.basicConfig(handlers=[handler], level=logging.INFO)
logging.info("This will rotate when the log file reaches 1KB.")
