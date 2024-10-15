print('Списковые, словарные сборки')

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# В переменную first_result запишите список созданный при помощи сборки состоящий из длин строк списка first_strings,
# при условии, что длина строк не менее 5 символов.

first_result = [item for item in first_strings if len(item) > 5]
print(first_result)

# В переменную second_result запишите список созданный при помощи сборки состоящий из пар слов(кортежей) одинак. длины.
# Каждое слово из списка first_strings должно сравниваться с каждым из second_strings. (два цикла)

second_result = [(item_fs, item_ss) for item_fs in first_strings for item_ss in second_strings
                 if len(item_fs) == len(item_ss)]
print(second_result)

# В переменную third_result запишите словарь созданный при помощи сборки, где парой ключ-значение будет строка-длина
# строки. Значения строк будут перебираться из объединённых вместе списков first_strings и second_strings.
# условие записи пары в словарь - чётная длина строки.

third_result = {key: len(key) for key in first_strings + second_strings if not len(key) % 2}
print(third_result)



