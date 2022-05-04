import sys
input = sys.stdin.readline

n = int(input())
the_stack = []
command_list = []
step = 0
cur_num = 1
is_stack = True
while step < n:
    try:
        input_num = int(input())
        if cur_num <= input_num:
            for num in range(cur_num, input_num+1):
                the_stack.append(num)
                command_list.append('+')
                cur_num += 1
            else:
                the_stack.pop()
                command_list.append('-')
        else:
            for _ in range((the_stack[-1] + 1) - input_num):
                the_stack.pop()
                command_list.append('-')
        step += 1
    except IndexError:
        is_stack = False
        break

if is_stack:
    for operator in command_list:
        print(operator)
else:
    print('NO')