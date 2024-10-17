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
