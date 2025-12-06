import sys

sys.path.append("../constants")
from character_constants import *
from text_constants import *


def calculate(task: str) -> str:
    """This function is the interface for calculating expressions."""
    if len(task) == 0:
        return ""

    task = check_first_character(task)

    task_list = split_task(task)
    task_list = adapt_first_number_if_negative(task_list)
    task_list = calculate_with_multiply_and_divide(task_list)

    if task_list == TEXT_INVALID_SYNTAX:
        return TEXT_INVALID_SYNTAX

    return calculate_with_add_and_substract(task_list, task)


def calculate_with_add_and_substract(task_list, task):
    result = 0

    for index, element in enumerate(task_list):
        if index > len(task_list) - 1:
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


def calculate_with_multiply_and_divide(task_list):
    task_list_with_multiply_and_divide_calculated = []

    for element in task_list:
        remember_operation = ""
        store_element_before = ""
        store_element_after = ""

        if is_not_multiply_or_divide_expression(element):
            task_list_with_multiply_and_divide_calculated.append(element)
            continue

        for index, character in enumerate(element):
            if (index == 0):
                store_element_before = character
                continue
            if (is_last_index(index, element)):
                store_element_after += character
                if (is_multiply_operator(remember_operation)):
                    result = multiply(store_element_before, store_element_after)
                    if (is_error_result(result)):
                        return result
                    task_list_with_multiply_and_divide_calculated.append(result)
                elif (is_divide_operator(remember_operation)):
                    result = divide(store_element_before, store_element_after)
                    if (is_error_result(result)):
                        return result
                    task_list_with_multiply_and_divide_calculated.append(result)
            elif (is_multiply_or_division_operator(character)) and (remember_operation != ""):
                if (is_multiply_operator(remember_operation)):
                    result = multiply(store_element_before, store_element_after)
                elif (is_divide_operator(remember_operation)):
                    result = divide(store_element_before, store_element_after)
                if (is_error_result(result)):
                    return result
                store_element_before = result
                store_element_after = ""
                remember_operation = character
            elif is_multiply_or_division_operator(character):
                remember_operation = character
            elif remember_operation != "":
                store_element_after += character
            else:
                store_element_before += character
    return task_list_with_multiply_and_divide_calculated

def is_multiply_or_division_operator(character):
    return character == CHARACTER_MULTIPLY or character == CHARACTER_DIVISION

def is_multiply_operator(character):
    return character == CHARACTER_MULTIPLY

def is_divide_operator(character):
    return character == CHARACTER_DIVISION

def is_error_result(result):
    return result == TEXT_INVALID_SYNTAX

def is_not_multiply_or_divide_expression(element):
    return element == CHARACTER_PLUS or element == CHARACTER_MINUS or (
                element.find(CHARACTER_MULTIPLY) == -1 and element.find(CHARACTER_DIVISION) == -1)


def is_last_index(index, element):
    return index == len(element) - 1


def multiply(element_one, element_two):
    result = ""
    try:
        result = float(element_one) * float(element_two)
    except:
        return TEXT_INVALID_SYNTAX
    return str(result)


def divide(element_one, element_two):
    result = ""
    try:
        result = float(element_one) / float(element_two)
    except:
        return TEXT_INVALID_SYNTAX
    return str(result)


def split_task(task):
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