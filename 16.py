def F(n):
    if n <= 1:
        return 0
    if n % 2 == 0:
        return 2 * F(n - 1) + 1
    return (n + 1) // 2 + F(n - 1)

print(F(33))
