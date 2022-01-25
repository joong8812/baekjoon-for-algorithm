def d(n):
    result = n
    for i in range(4):
        result += (n // 10 ** i) % 10
    return result

a = set(x for x in range(1, 10001))
b = set(d(x) for x in range(1, 10001))

for i in sorted(a-b):
    print(i)
