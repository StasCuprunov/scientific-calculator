import sys
sys.path.append("../constants")
from character_constants import *
from text_constants import *

# calculation interface
def calculate(task: str) -> str:
    if len(task) == 0:
        return ""
        
    task = check_first_character(task)

    task_list = split_task_line_calculation(task)
    task_list = adapt_first_number_if_negative(task_list)

    task_list = calculate_with_multiply_and_division(task_list)

def calculate_with_list(task_list, task):
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
            elif element == CHARACTER_MULTIPLY:
                result = result * float(task_list[index + 1])
                index += 1
            elif element == CHARACTER_DIVISION:
                result = result / float(task_list[index + 1])
                index += 1
        except:
            return TEXT_INVALID_SYNTAX
    if (result == 0):
        return task
    return str(result)
    
def calculate_with_multiply_and_division(task_list):
    task_list_with_multiply_and_division_calculated = []
    
    for element in task_list:
        remember_operation = ""
        store_element_before = ""
        store_element_after = ""

        for index, character in enumerate(element):
            
            if (index == 0):
                store_element_before = character
                continue
            if character == CHARACTER_MULTIPLY and remember_operation != "":
                result = float(store_element_before) * float(store_element_after)
                task_list_with_multiply_and_division_calculated.append(str(result))
                store_element_before = ""
                store_element_after = ""
            elif (character == CHARACTER_DIVISION) and (remember_operation != ""):
                result = float(store_element_before) / float(store_element_after)
                task_list_with_multiply_and_division_calculated.append(str(result))
                store_element_before = ""
                store_element_after = ""
            elif character == CHARACTER_MULTIPLY or character == CHARACTER_DIVISION:
                remember_operation = character
            elif (index == len(element) - 1):
                store_element_after += character
                if (remember_operation == CHARACTER_MULTIPLY):
                    result = float(store_element_before) * float(store_element_after)
                    task_list_with_multiply_and_division_calculated.append(str(result))
                elif (remember_operation == CHARACTER_DIVISION):
                    result = float(store_element_before) / float(store_element_after)
                    task_list_with_multiply_and_division_calculated.append(str(result))
            elif remember_operation != "":
                store_element_after += character
            else:
                store_element_before += character
    print(task_list_with_multiply_and_division_calculated)
"""for element in task_list:
        store_element = ""
        for index, character in enumerate(element):
            if (index == 0):
                store_element = element
            if (element == CHARACTER_PLUS or element == CHARACTER_MINUS):
                result = 0
                if (remember_operation == CHARACTER_MULTIPLY):
                    result = float(store_element_before) * float(store_element_after)
                elif (remember_operation == CHARACTER_DIVISION):
                    result = float(store_element_before) / float(store_element_after)
                task_list_with_point_calculation.append(result)
            
                store_element_before = ""
                store_element_after = ""
                remember_operation = ""
                task_list_with_point_calculation.append(element)
            elif ((element == CHARACTER_MULTIPLY or element == CHARACTER_DIVISION)
                  and remember_operation != ""):
                if (remember_operation == CHARACTER_MULTIPLY):
                    store_element_before = str(float(store_element_before) * float(store_element_after))
                elif remember_operation == CHARACTER_DIVISION:
                    store_element_before = str(float(store_element_before) / float(store_element_after))
                store_element_after = ""
                remember_operation = element
            elif (element == CHARACTER_MULTIPLY or element == CHARACTER_DIVISION):
                remember_operation = element
        
            if (remember_operation == ""):
                store_element_before += element
            else:
                store_element_after += element
        """

def split_task_line_calculation(task):
    task_list = []
    store_element = ""
    
    for index, character in enumerate(task):
        if (index == 0 and character == CHARACTER_MINUS):
            task_list.append(CHARACTER_MINUS)
            continue
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