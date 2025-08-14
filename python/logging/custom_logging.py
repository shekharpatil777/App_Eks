import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logging.debug("Debugging details")
logging.info("Application started")
logging.error("Something went wrong!")
