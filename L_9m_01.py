
print('До списковых сборок')

def mult(x):
    return x * 2

def odd(x):
    y = x % 2
    print(y, end=' ')       # 0 0 1 0
    return y                # 5
# Эта функция возвращает результат выражения x % 2, которое вычисляет остаток от деления x на 2. Если x является
# нечётным числом, то остаток будет равен 1, что в контексте Python считается истинным (True). Если x является чётным
# ислом, остаток будет 0, что считается ложным (False). Таким образом, функция odd(x) возвращает True для нечётных
# чисел и False для чётных.

l = [2, 4, 5, 6]

result = map(mult, l)
print(list(result))                     # [4, 8, 10, 12]
result = map(mult, filter(odd, l))      # [10]
print(list(result))


print('Списковые сборки')

l = [2, 4, 5, 6]

list_com_01 = [item * 2 for item in l]
print(list_com_01)

list_com_02 = [l[i] * 2 for i in range(len(l))]
print(list_com_02)

list_com_03 = [l[i] * 2 for i in range(3)]
print(list_com_03)

list_com_04 = [item * 2 for item in l if item > 4]
print(list_com_04)                                                      # [10, 12]

list_com_05 = [item * 2 for item in l if item % 2]
print(list_com_05)                                                      # [10]

list_com_06 = [item * 2 if item % 2 else item * 3 for item in l]        # [6, 12, 10, 18]
print(list_com_06)

l = [2, 4, 'Oleg', 5, 6]

list_com_07 = [item if type(item) == str else item * 5 for item in l]   # [10, 20, 'Oleg', 25, 30]
print(list_com_07)

print('Вложенные списки')

l = [2, 4, 5, 6]
m = [10, 20, 40]

list_com_08 = [x * y for x in l for y in m]                     # [20, 40, 80, 40, 80, 160, 50, 100, 200, 60, 120, 240]
print(list_com_08)

list_com_09 = [x * y for x in l for y in m if x % 2]            # [50, 100, 200]
print(list_com_09)

list_com_09 = [x * y for x in l for y in m if x % 2 and y != 20] # [50, 200]
print(list_com_09)

print('Множества и словари')

l = [12, 4, 9, 5, 6, 3, 4, 4]

list_com_10 = {x for x in l}                                    # {3, 4, 5, 6, 9, 12}
print(list_com_10)

list_com_11 = {x: x * 2 for x in l}                             # {12: 24, 4: 8, 9: 18, 5: 10, 6: 12, 3: 6}
print(list_com_11)


print('Генераторы')




