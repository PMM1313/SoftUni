def func_executor(*args):
    result = []
    for func, data in args:
        result.append(f"{func.__name__} - {func(*data)}")

    return "\n".join(result)

def sum_numbers(num1, num2):

    return num1 + num2


def multiply_numbers(num1, num2):

    return num1 * num2


def make_upper(*strings):

    result = tuple(s.upper() for s in strings)

    return result

def make_lower(*strings):

    result = tuple(s.lower() for s in strings)

    return result

