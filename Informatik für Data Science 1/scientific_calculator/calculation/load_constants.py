import json
import os
import sys

sys.path.append("../constants")
from configuration_constants import *


def get_constants_for_calculation():
    with open(os.path.join("constants", "constants.json"), encoding="utf-8") as json_file:
        constants_from_json = json.load(json_file)
        constants_for_calculation = constants_from_json["constants"]
        dictionary_for_constants = {}
        number_of_decimal_points = NUMBER_OF_DECIMAL_POINTS
        for element in constants_for_calculation:
            format_number = "{:." + str(number_of_decimal_points) + "f}"
            number = format_number.format(element["value"])
            dictionary_for_constants[element["si-symbol"]] = remove_unnecessary_digits(number)

        return dictionary_for_constants

def remove_unnecessary_digits(number):
    return str(number).rstrip("0")