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