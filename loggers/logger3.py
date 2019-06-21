import logging

logging.basicConfig(
    format="%(process)d-%(name)s-%(levelname)s-%(message)s-%(asctime)s",
    level=logging.INFO,
)
logging.warning("This is a warning")
logging.info("Admin logged in")
logging.error("Error time")
