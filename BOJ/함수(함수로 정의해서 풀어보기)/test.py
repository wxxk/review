a = [1, 2, 3]
b = [3, 4, 5]

for i in range(len(b)):
    a.append(b[i])

print(set(a) - set(b))