import logging

#Logging Exceptions
try:
    1 / 0
except ZeroDivisionError:
    logging.exception("Exception occurred")
