import json

firms_profit = {}
total_profit = 0
profit_count = 0

with open("firms.txt", "r", encoding="utf-8") as f:
    for line in f:
        name, form, vyruchka_str, isderzski_str = line.split()

        profit = float(vyruchka_str) - float(isderzski_str)

        firms_profit.update({name: profit})

        if profit > 0:
            total_profit += profit
            profit_count += 1

avg_profit = total_profit / profit_count if profit_count else 0

res = [firms_profit, {"avg_profit": avg_profit}]

with open("firms.json", "w", encoding="utf-8") as j_f:
    json.dump(res, j_f, ensure_ascii=False)

print(res)