# test_case = int(input())
# case = 0

# while case < test_case:
#     start, end = map(int, input().split())
#     d = end - start

#     n = 1
#     while True:
#         if d <= n * (n+1):
#             break
#         n += 1

#     if d <= n ** 2:
#         print(2*n - 1)
#     else:
#         print(2*n)

#     case += 1


import math
T = int(input())
for i in range(T):
    x,y = map(int,input().split())
    space = (y-x)
    z = int(math.sqrt(space))
    if space > z*(z+1):
        time = 2*z + 1
    elif space == z**2:
        time = 2*z -1
    else:
        time = 2*z
        
    print(time)