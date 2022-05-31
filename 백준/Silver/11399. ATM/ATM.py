n = int(input())
p_list = list(map(int, input().split()))
p_list.sort()
sum = 0
for i, num in enumerate(p_list):
    sum += num * (len(p_list) - i)
print(sum)