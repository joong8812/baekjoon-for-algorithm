hm = list(map(int, input().split()))
h = hm[0]
m = hm[1]

if m < 45:
    h -= 1
    if h < 0:
        h = 24 + h
    m = (60+m) - 45
else:
    m = m - 45

print(h, m)