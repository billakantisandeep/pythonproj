# Program related to capturing the stack traces.

import logging

a = 5
b = 0

try:
    c = a / b
# except Exception as e:
#     logging.error("Execption occurred", exc_info=True)
except Exception as e:
    logging.exception("Execption occured")
