def d(n):
    result = n
    result += n // 1000
    result += (n // 100) % 10
    result += (n // 10) % 10
    result += n % 10
    return result

a = set(x for x in range(1, 10001))
b = set(d(x) for x in range(1, 10001))

for i in sorted(a-b):
    print(i)
