print('Декораторы в Python')

# Напишите 2 функции:
# Функция, которая складывает 3 числа (sum_three)
# Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и "Составное" в противном случае.
# Пример:
# result = sum_three(2, 3, 6)
# print(result)
def is_prime(fun_time):
    def checking_numbers(*args):
        result = fun_time(*args)
        is_prime = True
        if result < 2:
            is_prime = False
        from math import sqrt
        for i in range(2, int(sqrt(result)) + 1):
            if result % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f'{result} - Простое')
        else:
            print(f'{result} - Составное')
        return result
    return checking_numbers

@is_prime
def sum_them_all(*args):
    return sum(args)


result = sum_them_all(2, 3, 6, 1)
print(result)

