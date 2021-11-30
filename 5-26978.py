for i in range(1, 100):
    N = 109 - i
    b = bin(N)[2:]
    if N % 2 == 0:
        b += '10'
    else:
        b += '01'
    R = int(b, 2)
    if R < 109:
        print(R)
        break

