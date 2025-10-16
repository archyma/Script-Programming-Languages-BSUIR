with open("clients.txt", "r") as f:
    suma = sum(int(line.split()[1]) for line in f)
    print(suma)
    f.seek(0)

    for line in f:
        data = line.split()
        if int(data[1]) == 0:
            print(f"Клиент без вложений: {data[0]}")