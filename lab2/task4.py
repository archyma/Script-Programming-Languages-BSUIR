a = 0
b = 0

try:
    a = int(input('Введите число: '))
    b = int(input('Введите число: '))
except ValueError as e:
    print(e)
else:
    print(a)
finally:
    print('Спасибо за вклад!')

try:
    print(a / b)
except ZeroDivisionError as e:
    print(e)

l = list(range(10))

i = int(input('Номер: '))
try:
    print(l[i])
except IndexError as e:
    print(e)