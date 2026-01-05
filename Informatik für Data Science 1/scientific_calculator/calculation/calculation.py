import sys

sys.path.append("../constants")
from text_constants import *

def calculate(task: str) -> str:
    """This function is the interface for calculating expressions."""
    if len(task) == 0:
        return ""
    try:
        return eval(task)
    except:
        return TEXT_INVALID_SYNTAX
