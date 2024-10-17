print('Функциональное разнообразие')

print('Lambda-функция:')

first = 'Мама мыла раму'
second = 'Рамена мало было'


result = list(map(lambda x, y: x == y, first, second))
print(result)

print('Замыкание:')

def get_advanced_writer(file_name):
     def write_everything(*data_set):
          with open(file_name, 'a', encoding='utf-8') as file:
               for item in data_set:
                    file.write(f'{item}\n')
     return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

print('Замыкание по chatGPT')

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for item in data_set:
                if isinstance(item, (list, tuple)):  # Проверяем, является ли элемент итерируемым (но не строкой)
                    for sub_item in item:
                        file.write(f'{sub_item}\n')
                else:
                    file.write(f'{item}\n')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Ваш код в целом выглядит правильно, но есть небольшая проблема в том, как вы обрабатываете элементы, переданные в
# data_set. Если вы передаете элементы, которые являются списком,
# такие как ['А', 'это', 'уже', 'число', 5, 'в', 'списке'], то ваша функция запишет этот список как «строку» в файле
# (например, ['А', 'это', 'уже', 'число', 5, 'в', 'списке']), а не каждый элемент по отдельности.

# Если вы хотите записывать каждый элемент списка отдельно, вам нужно будет обработать каждый элемент в data_set,
# проверяя, является ли он итерируемым объектом (таким как список) или нет. Если это так, нужно распаковать его
# элементы и записать их по одному.

print('Метод __call_')

from typing import Union
from random import choice

class MysticBall:
    def __init__(self, *words: Union[list, tuple, set]):
        self.words = words

    def __call__(self, ):
        return choice(self.words)

# Ваш класс здесь
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())

# Метод __call__:
# Создайте класс MysticBall, объекты которого обладают атрибутом words хранящий коллекцию строк.
# В этом классе определите метод __call__ который будет случайным образом выбирать слово из words и возвращать его.
# Для случайного выбора с одинаковой вероятностью для каждого данного в коллекции можете использовать функцию choice
# из модуля random.
# Ваш код (количество слов для случайного выбора может быть другое):
# from random import choice
