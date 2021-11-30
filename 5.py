for i in range(128, 255):
    b = bin(i)[2:]
    b = b.replace('0', '2').replace('1', '0').replace('2', '1')
    b = int(b, 2)
    if i - b == 105:
        print(i)
        break
