m, n = map(int, input().split())
prime_num_list = [0] * (10**6)
prime_num_list[1] = 1

for i in range(2, n+1):
    for j in range(2, n+1):
        if i * j > n:
            break
        prime_num_list[i*j] = 1

for num in range(m, n+1):
    if prime_num_list[num] == 0:
        print(num)

# 다른분 코드1
# from collections import deque
#
# m,n = map(int,input().split())
# sosu = deque()
# sosu.append(2)
# sosu.append(3)
#
# for p in range(5,n+1,2):
#     for q in range(len(sosu)):
#         if p >= (sosu[q]*sosu[q]) and p%sosu[q]==0:
#
#             break
#         if p < (sosu[q]*sosu[q]):
#
#             sosu.append(p)
#             break
# while sosu:
#     a = sosu.popleft()
#     if a >= m and a<=n :
#         print(a)


# 다른분 코드2
# import math
#
# m, n = map(int, input().split())
#
#
# def search_prime_number(m, n):
#     sieve = [True] * (n + 1)
#     prime_numbers = []
#
#     k = int(math.sqrt(n))
#     for i in range(2, k + 1):
#         if sieve[i] == True:
#             for j in range(i + i, n + 1, i):
#                 sieve[j] = False
#
#     for i in range(m, n + 1):
#         if i == 1:
#             sieve[i] = False
#         if sieve[i] == True:
#             prime_numbers.append(i)
#     return prime_numbers
#
#
# prime_list = search_prime_number(m, n)
# for n in prime_list:
#     print(n)