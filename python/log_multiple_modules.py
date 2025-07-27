# In main.py
import logging
import module

logging.basicConfig(level=logging.INFO)
logging.info("Main logger")

# In module.py
import logging

logger = logging.getLogger(__name__)
logger.info("Module logger")
