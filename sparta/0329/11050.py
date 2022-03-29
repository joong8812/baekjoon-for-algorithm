'''
# 이항 계수 1
자연수 \(N\)과 정수 \(K\)가 주어졌을 때 이항 계수 
\(\binom{N}{K}\)를 구하는 프로그램을 작성하시오.


[입력]
첫째 줄에 \(N\)과 \(K\)가 주어진다. (1 ≤ \(N\) ≤ 10, 0 ≤ \(K\) ≤ \(N\))

[출력]

\(\binom{N}{K}\)를 출력한다.

[예제 입력]
5 2

[예제 출력]
10

link: https://www.acmicpc.net/problem/11729
'''
n,k = map(int, input().split())
parent_num = 1
for num in range(n-k+1, n+1):
    parent_num *= num
    
child_num = 1
for num in range(1, k+1):
    child_num *= num
print(parent_num // child_num)