'''
The purpose of this project was to serve as an introduction to Flask. This lesson explained the __main__ and __name__ attributes,
emphasized the use of nesting functions, and explained Python decorators and the @ syntax.
'''

import time


def speed_calc_decorator(function):
    def wrapper():
        start_time = time.time()
        result = function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time - start_time}s")
        return result
    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


fast_function()
slow_function()
