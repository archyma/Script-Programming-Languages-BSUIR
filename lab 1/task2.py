st = input("Введите строку\n")

for char in st:
    print(ord(char))

st1 = st.split()
print(f"Самое длинное слово в строке - {max(st1, key=len)}")