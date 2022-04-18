import sys
input = sys.stdin.readline

N = int(input())

num_group = [int(input()) for _ in range(N)]
print(round(sum(num_group)/N))
sorted_num_group = sorted(num_group)
print(sorted_num_group[int((N-1)/2)])

# 최빈값
if N > 1:
    num_dict = {}
    for n in sorted_num_group:
        if n in num_dict:
            num_dict[n] += 1
        else:
            num_dict[n] = 1
    sorted_num_dict = sorted(num_dict.items(), key=lambda item:item[1], reverse=True)
    if sorted_num_dict[0][1] == sorted_num_dict[1][1]:
        print(sorted_num_dict[1][0])
    else:
        print(sorted_num_dict[0][0])
else:
    print(sorted_num_group[0])

print(max(sorted_num_group) - min(sorted_num_group))