a = 1

d = 0
h = 0
m = 0
s = 0

while a != 0:
    a = int(input("Введите количество секунд\n"))
    if a > 0:
        s = a
        m = s // 60
        s %= 60
        h = m // 60
        m %= 60
        d = h // 24
        h %= 24
        print(f"{d}:{h}:{m}:{s}")
    elif a < 0:
        print("Неправильный ввод?\nПопробуйте снова\n")
    else:
        print("все, наигрались")