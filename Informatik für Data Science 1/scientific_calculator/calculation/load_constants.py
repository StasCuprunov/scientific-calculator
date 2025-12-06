import json
import os

def get_constants_for_calculation():
    with open(os.path.join("constants", "constants.json"), encoding="utf-8") as json_file:
        constants_for_calculation = json.load(json_file)
        dictionary_for_constants = {}

        for element in constants_for_calculation["constants"]:
            dictionary_for_constants[element["si-symbol"]] = element["value"]
        return dictionary_for_constants