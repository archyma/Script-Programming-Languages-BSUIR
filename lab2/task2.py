def task2(argument):
    # match argument:
    #     case 1:
    #
    if isinstance(argument, list):
        print('Лист')
        argument = [i for i in argument if i != 0]

        last_pos_ind = None
        for i in range(len(argument)):
            if argument[i] > 0:
                last_pos_ind = i

        if last_pos_ind is not None and last_pos_ind < len(argument) - 1:
            return sum(argument[last_pos_ind + 1:])
        else:
            return 0

    elif isinstance(argument, dict):
        print('Словарь')
        return min(argument.items(), key=lambda x: x[1])

    elif isinstance(argument, (int, float)):
        print('Число')
        return str(argument)[::-1]

    elif isinstance(argument, str):
        print('Строка')
        return len(argument.split())

    else:
        return 'функция не работает'



print(task2([0,3,5,2,-5,8,-4,7,-8,0,-2,0,-5]))
print(task2({'a':5,'b':2,'c':9}))
print(task2(123456789))
print(task2('Я люблю прогуливать пары и спать'))