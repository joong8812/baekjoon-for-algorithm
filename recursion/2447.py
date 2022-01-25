# num = int(input())
#
#
# def make_star(i, j, n):
#     if (i / n) % 3 == 1 and (j / n) % 3 == 1:
#         print(' ', end="")
#     else:
#         if i % 3 == 1 and j % 3 == 1:
#             print(" ", end="")
#         else:
#             print("*", end="")
#
#
# for i in range(num):
#     for j in range(num):
#         make_star(i, j, num)
#     print()
import sys

sys.setrecursionlimit(10 ** 6)


def append_star(LEN):
    if LEN == 1:
        return ['*']
    Stars = append_star(LEN // 3)
    print(Stars)
    L = []
    for S in Stars: L.append(S * 3)
    for S in Stars: L.append(S + ' ' * (LEN // 3) + S)
    for S in Stars: L.append(S * 3)
    print(L)
    return L

n = int(sys.stdin.readline().strip())
print('\n'.join(append_star(n)))


# https://cotak.tistory.com/38
# https://cryptosalamander.tistory.com/38
# https://st-lab.tistory.com/95

# 명준님꺼
def star(n):
    arr = making_star_arr(n)
    print_star(arr, n)


def print_star(arr, num):
    idx = 0
    while idx < len(arr):
        if idx%(num/3) == (num/3 - 1):
            print(arr[idx])
        else:
            print(arr[idx], end='')
        idx += 1

def making_star_arr(num):
    idx = 0
    result = []
    if num == 3:
        return ['***','* *','***']
    else:
        arr = making_star_arr(int(num/3))
        b = int(num/9)
        c = len(arr)
        while idx < num:
            if idx//int(num/3) == 1:
                for a in arr[(idx*b)%c:((idx*b)%c)+b]:
                    result.append(a)
                for j in range(b):
                    result.append('   ')
                for a in arr[(idx*b)%c:((idx*b)%c)+b]:
                    result.append(a)
            else:
                for j in range(3):
                    for a in arr[(idx*b)%c:((idx*b)%c)+b]:
                        result.append(a)
            idx += 1
        return result

star(int(input()))