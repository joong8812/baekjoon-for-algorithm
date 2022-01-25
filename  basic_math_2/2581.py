m = int(input())
n = int(input())
prime_num_list = [2, 3]
for num in range(4, n+1):
    for p_num in prime_num_list:
        if num % p_num == 0:
            break
    else:
        prime_num_list.append(num)

answer_list = []
for num in range(m, n+1):
    for p_num in prime_num_list:
        if num == p_num:
            answer_list.append(num)
        if num % p_num == 0 or num < p_num:
            break
    else:
        answer_list.append(num)

if len(answer_list) == 0:
    print("-1")
else:
    print(sum(answer_list))
    print(min(answer_list))