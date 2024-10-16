print('Генераторные сборки')

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# В переменную first_result запишите генераторную сборку, которая высчитывает разницу длин строк из списков first и
# second, если их длины не равны. Для перебора строк попарно из двух списков используйте функцию zip.

first_result = (len(item_f) - len(item_s) for item_f, item_s in zip(first, second) if len(item_f) != len(item_s))
print(list(first_result))

# В переменную second_result запишите генераторную сборку, которая содержит результаты сравнения длин строк в
# одинаковых позициях из списков first и second. Составьте эту сборку НЕ используя функцию zip. Используйте функции
# range и len.

second_result = (len(first[i]) == len(second[i]) for i in range(min(len(first), len(second))))
print(list(second_result))

print('Учитываем количество элементов по максимуму')

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер', 'Python']

second_result_ = (len(first[i]) == len(second[i]) if i < len(first) and i < len(second) else False for i in
                  range(max(len(first), len(second))))
print(list(second_result_))
