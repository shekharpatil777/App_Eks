# In main.py
import logging
import module

#Log from Multiple Modules
logging.basicConfig(level=logging.INFO)
logging.info("Main logger")

# In module.py
import logging

logger = logging.getLogger(__name__)
logger.info("Module logger")
