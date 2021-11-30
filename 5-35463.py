for i in range(100, 1000):
    b = bin(i)[2:]
    for j in range(3):
        c0 = b.count('0')
        c1 = b.count('1')
        if c0 == c1:
            b += b[-1]
        else:
            b += '1' if c1 < c0 else '0'
    if int(b, 2) % 4 == 0:
        print(i)
        break
