import math

a, b, v = map(int, input().split())
day = math.ceil((v-b) / (a-b))
print(day)