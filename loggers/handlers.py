# this program for ilustrating logs sent to a handler.
import logging

# Create a custom logger
logger = logging.getLogger(__name__)

# Create Handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler("file.log")
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# Create Formatter and add to handlers.
c_format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
f_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(messasge)s")
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning(
    "This is a warning"
)  # Creates a logrecord that holds all the information of the event passing to the handlers
logger.error(
    "This is an error"
)  # c_handler -- as same before. h_handler -- prints to file.

