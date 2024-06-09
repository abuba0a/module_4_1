print('Арифметическая версия')
print('Введите первую пару чисел')
a = input('a = ')
b = input('b = ')

print('Введите вторую пару чисел')
c = input('c = ')
d = input('d = ')


def fake_divide(*arg):
    first = int(a)
    second = int(b)
    if second == 0:
        result1 = 'Ошибка'
    else:
        result1 = first / second


    first = int(c)
    second = int(d)
    if second == 0:
        result2 = 'Ошибка'
    else:
        result2 = first / second
    print('Результат = ', result1)
    print('Результат = ', result2)


fake_divide()

