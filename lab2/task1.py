def is_ann(word1, word2):
    # return sorted(word1) == sorted(word2)
    return len(word1) == len(word2) and set(word1.upper()) == set(word2.upper())

print(is_ann('егор', 'гоер'))
print(is_ann('wrbd', 'dbwq'))
print(is_ann('БГУИР', 'бгуир'))
print(is_ann('Алежа', 'АлежаАлежа'))