def return_10():
    return 10

def add(num_1, num_2):
    add_result = num_1 + num_2
    return add_result

def subtract(num_1, num_2):
    subtract_result = num_1 - num_2
    return subtract_result

def multiply(num_1, num_2):
    multiply_result = num_1 * num_2
    return multiply_result

def divide(num_1, num_2):
    divide_result = num_1 / num_2
    return divide_result

def length_of_string(string):
    string_length = len(string)
    return string_length

def join_string(string_1, string_2):
    join_string = string_1 + string_2
    return join_string

def add_string_as_number(string_1, string_2):
    add_result = int(string_1) + int(string_2)
    return add_result

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
  
def number_to_full_month_name(month_number):
    return months[month_number -1]


def number_to_short_month_name(month_number):
    full_month = number_to_full_month_name(month_number)
    return full_month[:3]