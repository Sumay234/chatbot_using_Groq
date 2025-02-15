import sys
import os
# from src.logger import logging
from logger import get_logger

class CustomException(Exception):
    """Custom Exception class to handle exceptions with traceback details."""
    
    def __init__(self, message: str, error: Exception):
        super().__init__(message)
        _, _, exc_tb = sys.exc_info()
        self.error_details = f"{error} at line {exc_tb.tb_lineno} in {exc_tb.tb_frame.f_code.co_filename}"

    def __str__(self):
        return f"{super().__str__()} - {self.error_details}"


'''import sys
from src.logger import logging


def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno, str(error)
    )
    
    return error_message

class CustomException(Exception):
    
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)
        
    def __str__(self):
        return self.error_message'''