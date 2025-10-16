with open("F1.txt", "w") as f1:
    while True:
        line = input("Введите строку: ")
        if line == "":
            break
        f1.write(line + "\n")

with open("F1.txt", "r") as f1, open("F2.txt", "w+") as f2:
    for line in f1:
        if not any(i.isdigit() for i in line):
            f2.write(line)

    f2.seek(0)
    lines = f2.readlines()
    if lines:
        print(f"Кол-во слов в последней строке: {len(lines[-1].split())}")
    else:
        print("Нет")