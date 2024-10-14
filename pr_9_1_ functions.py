print('Задача "Вызов разом"')

from typing import Union, List, Callable

print('Вариант 1')

def apply_all_func(int_list: List[Union[int, float]], *functions: Callable):
    results = {}
    for function in functions:
        key = function.__name__
        results[key] = function(int_list)
    return results

# def min_(int_list):
#     return min(int_list)
#
# def max_(int_list):
#     return max(int_list)
#
# def len_(int_list):
#     return len(int_list)
#
# def sum_(int_list):
#     return sum(int_list)
#
# def sorted_(int_list):
#     return sorted(int_list)


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

print('Вариант 2')

def apply_all_func(int_list: List[Union[int, float]], *functions: Callable):
    results = {}
    for function in functions:
        key = function.__name__
        results[key] = function(int_list)
    return results

def min_(int_list):
    return min(int_list)

def max_(int_list):
    return max(int_list)

def len_(int_list):
    return len(int_list)

def sum_(int_list):
    return sum(int_list)

def sorted_(int_list):
    return sorted(int_list)


print(apply_all_func([6, 20, 15, 9], max_, min_))
print(apply_all_func([6, 20, 15, 9], len_, sum_, sorted_))



