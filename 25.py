a = []
for i in range(12014, 49636):
    if i % 13 == 7 and i % 5 != 0 and i % 12 != 0:
        a.append(i)
print(a[0], len(a))
