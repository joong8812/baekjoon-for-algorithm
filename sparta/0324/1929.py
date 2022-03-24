'''
# 소수 구하기
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

[입력]
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

[출력]
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

[예제 입력]
3 16

[예제 출력]
3
5
7
11
13

link: https://www.acmicpc.net/problem/1929
'''
def get_prime_numbers(end):
    all_numbers = [True] * (end+1)
    all_numbers[0] = False
    all_numbers[1] = False
    
    for num in range(2, end+1):
        if all_numbers[num] == True:
            variable_num = 2
            while num*variable_num <= end:
                all_numbers[num*variable_num] = False
                variable_num += 1
    prime_numbers = []
    for num, is_prime in enumerate(all_numbers):
        if is_prime:
            prime_numbers.append(num)
    return prime_numbers
    
start, end = map(int, input().split())
for prime_number in get_prime_numbers(end):
    if prime_number >= start:
        print(prime_number)