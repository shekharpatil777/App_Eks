import logging

#Disable Logging Temporarily
logging.disable(logging.CRITICAL)  # Disable all logging
logging.warning("This won't show")
logging.disable(logging.NOTSET)    # Enable logging again
