numbers = input("Введите числа чрез запятую: ")

numList = numbers.split(',')

for i in numList:
    i = int(i)

numTuple = tuple(numList)

print(numList)
print(numTuple)