#Hoe to create your own logger.
import logging
logger = logging.getLogger(__name__)
logger.propagate = False # this will prevent the logger to run in the main module.
logger.info("Hello from logging helper.")