import sys
input = sys.stdin.readline

k = int(input())
step = 0
wrote_number = []
while step < k:
    input_num = int(input())
    if input_num == 0:
        if len(wrote_number) > 0:
            wrote_number.pop()
    else:
        wrote_number.append(input_num)
    step += 1
print(sum(wrote_number))