print('Версия высшей математики')
from math import inf
print('Введите первую пару чисел')
a = input('a = ')
b = input('b = ')

print('Введите вторую пару чисел')
c = input('c = ')
d = input('d = ')


def true_divide(*arg):
    first = int(a)
    second = int(b)
    if second == 0:
        result3 = inf
    else:
        result3 = first / second
    first = int(c)
    second = int(d)
    if second == 0:
        result4 = inf
    else:
        result4 = first / second
    print('Результат = ', result3)
    print('Результат = ', result4)


true_divide()
