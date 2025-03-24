def even_numbers(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return [el for el in result if el % 2 == 0]
    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers
