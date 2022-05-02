import sys
input = sys.stdin.readline

t = int(input())
case = 0
while case < t:
    stack_for_validation = []
    input_ps = input().rstrip()
    for character in input_ps:
        if character == '(':
            stack_for_validation.append('(')
        else:
            if len(stack_for_validation) != 0:
                stack_for_validation.pop()
            else:
                print('NO')
                break
    else:
        if len(stack_for_validation) == 0:
            print('YES')
        else:
            print('NO')
    case += 1