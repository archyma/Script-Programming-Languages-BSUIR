sub_dict = {}

with open("subjects.txt", "r", encoding="utf-8") as f:
    for line in f:
        subject, data = line.split(":")
        hours = 0

        for zan in data.split():
            number = ''.join(i for i in zan if i.isdigit())
            if number:
                hours += int(number)

        sub_dict.update({subject: hours})

print(sub_dict)