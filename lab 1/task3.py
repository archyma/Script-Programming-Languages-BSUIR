l = list()
s = 0
pr = 1

n = int(input("Введите длину списка\n"))

for i in range(n):
    l.append(int(input(f"Введите элемент {i+1}: ")) ** 3)
    s += l[i]
    pr *= l[i]

print("Список кубов в обратном порядке")
l.reverse()
print(l)
print(f"Сумма = {s}")
print(f"Произведение = {pr}")