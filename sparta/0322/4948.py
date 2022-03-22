'''
# 베르트랑 공준
베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.

이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.

예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)

자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오. 

[입력]
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 케이스는 n을 포함하는 한 줄로 이루어져 있다.

입력의 마지막에는 0이 주어진다.

[출력]
각 테스트 케이스에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력한다.

[예제 입력]
1
10
13
100
1000
10000
100000
0

[예제 출력]
1
4
3
21
135
1033
8392

link: https://www.acmicpc.net/problem/4948
'''

def get_count_prime_num(start, end):
    list = [True] * (end+1)

    for i in range(2, (end+1)):
        if list[i] == True:
            j = 2
            while (i*j) <= end:
                list[i*j] = False
                j += 1
    
    prime_num_count = 0
    for is_prime in list[start:]:
        if is_prime:
            prime_num_count +=1
        
    return prime_num_count

while (n := int(input())) != 0:
    print(get_count_prime_num(n+1, 2*n))
    