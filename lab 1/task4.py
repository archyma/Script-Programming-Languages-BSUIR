my_dict =  {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}

keys = []

for i in range(3):
    maxVal = my_dict.get('a')
    maxKey = 'a'
    for k, v in my_dict.items():
        if v > maxVal and k not in keys:
            maxKey = k
            maxVal = v
    keys.append(maxKey)

print("Ключи с максимальным значением:")
print(keys)