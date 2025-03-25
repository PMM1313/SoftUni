def logged(function):
    def wrapper(*args):
        result = function(*args)
        return f"you called {function.__name__}{args}\nit returned {result}"
    return wrapper





def func(a, b):
    return a + b


