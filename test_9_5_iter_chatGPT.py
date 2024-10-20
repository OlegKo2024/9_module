class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')
        self.step = step
        self.pointer = self.start
# Инициализация атрибутов — это процесс задания начальных значений переменным экземпляра (атрибутам) класса, когда
# создается объект этого класса. Этот процесс происходит в методе __init__(), который называется конструктором класса.
# Конструктор выполняется автоматически при создании нового объекта.
# Как это работает:
# Когда вы создаете объект, например:
# Python вызывает метод __init__() класса Iterator с аргументами -5 и 1 (в нашем случае step по умолчанию = 1)
#   Внутри метода __init__() происходит следующее:
    # 1. Определение атрибутов: Вы определяете, какие атрибуты будут у вашего класса - это start, stop, step и pointer.
    # 2. Присвоение значений: Вы присваиваете значения этим атрибутам:
    #       self.start = start      # здесь start = -5
    #       self.stop = stop        # здесь stop = 1
    #       self.step = step        # здесь step = 1 (по умолчанию)
    #       self.pointer = self.start  # здесь pointer = -5 (так как start = -5)
# self ссылается на текущий экземпляр класса. Таким образом, self.start, self.stop и другие атрибуты будут специфичны
# именно для этого экземпляра iter2.
    def __iter__(self):
        self.pointer = self.start
        return self
# Когда вы создаете объект, например, iter2:
    # iter2 становится объектом итератора, который управляет своей собственной логикой итерации. У него есть:
    # - Атрибут start: обозначает начальное значение итерации (в данном случае это -5).
    # - Атрибут stop: обозначает конечное значение итерации (в данном случае это 1).
    # - Атрибут step: обозначает шаг, с которым происходит итерация (по умолчанию это 1).
    # - Атрибут pointer: указывает на текущее значение, с которого начинается итерация (также устанавливается в start).
# Таким образом, каждый созданный вами объект Iterator — это независимый объект итератора, который можно
# использовать в циклах для обхода значений в установленном диапазоне, согласно заданному шагу.
# Объект итератора — это экземпляры класса <code>Iterator</code>, кроме iter2, это iter3, iter4 и iter5. Каждый из этих
# объектов имеет свои уникальные атрибуты, такие как start, stop, step и pointer. Они определяют начальную точку
# итерации, конечную точку, шаг и текущее положение в процессе итерации соответственно.

# Итерация по iter2:
# Когда создаем объект iter2 = Iterator(-5, 1) происходит инициализация атрибутов start, stop, step и pointer в __init__
# Затем используете его в цикле for i in iter2:, происходит следующее:
# - Вызов for i in iter2: вызывает метод __iter__(), который сбрасывает self.pointer на self.start, то есть на -5.
# - Затем цикл for вызывает метод __next__() , чтобы получить следующее значение.
# - В методе __next__() проверяется, не выходит ли pointer (который равен -5 на первом вызове) за пределы stop (1).
# Поскольку -5 меньше 1, итерация продолжается, pointer увеличивается на step (умолч. - 1), и возвращает новое значение
# - Этот процесс повторяется до тех пор, пока не будет достигнуто значение pointer, которое превышает значение stop
# (т.е. 1), после чего выбрасывается исключение StopIteration, и цикл завершает итерацию.

    def __next__(self):
        self.pointer += self.step
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration()
        return self.pointer

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()