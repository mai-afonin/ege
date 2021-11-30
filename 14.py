def dec2any(a, p):
    alph = 'ABCDEF'
    s = ''
    while a > 0:
        q = a % p
        if q >= 10:
            s = alph[q - 10] + s
        else:
            s = str(q) + s
        a //= p
    return s

for x in range(100):
    y = dec2any(81 ** 20 - 9 ** x + 50, 9)
    if sum([int(i) for i in y]) == 138:
        print(x)
        break
