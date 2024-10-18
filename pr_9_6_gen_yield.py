print('Генераторы')
from itertools import combinations, permutations
def all_variants(text):
    for i in range(len(text)+1):
        for j in combinations(text, i):
            yield ''.join(j)


a = all_variants("abc")
for i in a:
    print(i)


def all_variants(text):
    for i in range(len(text)+1):
        for j in permutations(text, i):
            yield ''.join(j)


a = all_variants("abc")
for i in a:
    print(i)
