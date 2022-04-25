import sys
input = sys.stdin.readline

yaksu_count = int(input())
num_list = list(map(int, input().split()))

# find max num
num_list.sort()
max_num = num_list[-1]
min_num = num_list[0]

print(max_num * min_num)