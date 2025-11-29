import sys
sys.path.append("../constants")
from character_constants import *
from text_constants import *

# calculation interface
def calculate(task: str) -> str:
    if len(task) == 0:
        return ""
        
    task = check_first_character(task)

    task_list = split_task(task)
    task_list = adapt_first_number_if_negative(task_list)

    return calculate_with_list(task_list)

def calculate_with_list(task_list):
    result = 0
    
    for index, element in enumerate(task_list):
        if index > len(task_list) - 2:
            break
        try:
            if (index == 0):
                result = float(element)
                continue
            if element == CHARACTER_PLUS:
                result = result + float(task_list[index + 1])
                index += 1
            elif element == CHARACTER_MINUS:
                result = result - float(task_list[index + 1])
                index += 1
        except:
            return TEXT_INVALID_SYNTAX
    if (result == 0):
        return task
    return str(result)

def split_task(task):
    task_list = []
    store_element = ""
    
    for character in task:
        if (character == CHARACTER_PLUS or character == CHARACTER_MINUS):
            task_list.append(store_element)
            task_list.append(character)
            store_element = ""
        else:
            store_element += character

    if (store_element != ""):
        task_list.append(store_element)
    return task_list

def adapt_first_number_if_negative(task_list):
    if len(task_list) > 1:
        if task_list[0] == CHARACTER_MINUS:
            task_list[1] = CHARACTER_MINUS + task_list[1]
            del task_list[0]
    return task_list

def check_first_character(task):
    first_character = task[0]
    if (first_character == CHARACTER_DECIMAL_POINT):
        return CHARACTER_ZERO + task
    elif (first_character == CHARACTER_PLUS):
        return task[1:]
    return task