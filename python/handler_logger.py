import logging

logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

# Console handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# File handler
fh = logging.FileHandler('custom.log')
fh.setLevel(logging.WARNING)

# Formatter
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# Add handlers
logger.addHandler(ch)
logger.addHandler(fh)

logger.info('Info to console only')
logger.warning('Warning to console and file')
