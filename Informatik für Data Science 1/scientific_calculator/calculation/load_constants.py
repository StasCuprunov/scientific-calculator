import json
import os

def get_constants_for_calculation():
    with open(os.path.join('constants', 'constants.json'), encoding="utf-8") as json_file:
        constants_for_calculation = json.load(json_file)

        return constants_for_calculation["constants"]