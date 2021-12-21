a = []
for line in open('17.txt').readlines():
    a.append(int(line))
b = [i % 160 for i in a]
c = [i % 7 for i in a]

s = 0
max_s = 0

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if b[i] != b[j] and (c[i] == 0 or c[j] == 0):
            s += 1
            if a[i] + a[j] > max_s:
                max_s = a[i] + a[j]

print(s, max_s)
