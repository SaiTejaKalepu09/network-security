import sys
from network_security.logging.logger import logging
class NetworkSecurityException(Exception):
    """Base class for exceptions in the network security module."""
    def __init__(self, error_message, error_details=sys):
        self.error_message = error_message
        _, _, exc_tb = error_details.exc_info()

        self.line_number = exc_tb.tb_lineno if exc_tb else None
        self.file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else None

    def __str__(self):
        return f"Error occurred in script: [{self.file_name}] at line number: [{self.line_number}] with error message: [{self.error_message}]"
        self.file_name, self.line_number, str(self.error_message)

if __name__ == "__main__":
    try:
        logging.info("This is a test log message.")
        a = 1/0
        raise ValueError("This is a test error.")
    except Exception as e:
        raise NetworkSecurityException(str(e), sys)
