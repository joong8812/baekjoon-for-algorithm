import sys
input = sys.stdin.readline

a, b = map(int, input().split())
if b > a:
  a, b = b, a
mok_list = []
a_left = 0
b_left = 0

while True:
  for n in range(2, b+1):
    if a % n == 0 and b % n == 0:
      mok_list.append(n)
      a = a // n
      b = b // n
      break
  else:
    break

all_mok_multiply = 1
for n in mok_list:
  all_mok_multiply *= n

print(all_mok_multiply)
print(all_mok_multiply*a*b)
