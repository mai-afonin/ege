max_A = 0
for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not ((39 != y + 2 * x) or (A < x) or (A < y)):
                flag = False
                break
        if not flag:
            break
    if flag:
        max_A = A
print(max_A)
