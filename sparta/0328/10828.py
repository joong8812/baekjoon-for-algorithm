'''
# 스택
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

[입력]
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 
주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

[출력]
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

[예제 입력]
14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top

[예제 출력]
2
2
0
2
1
-1
0
1
-1
0
3

link: https://www.acmicpc.net/problem/10828
'''
import sys
input = sys.stdin.readline
n = int(input())
my_stack = []
command_round = 0
while n > command_round:
    is_error = False
    input_command = input().strip()
    if 'push' in input_command:
        action, num = input_command.split()
        my_stack.append(int(num))
    else:
        if input_command == 'top':
            if len(my_stack) != 0:
                print(my_stack[-1])
            else:
                is_error = True
        elif input_command == 'pop':
            if len(my_stack) != 0:
                print(my_stack.pop())
            else:
                is_error = True
        elif input_command == 'size':
            print(len(my_stack))
        elif input_command == 'empty':
            print(1 if len(my_stack) == 0 else 0)
                
    if (is_error):
        print(-1)
    command_round += 1