init_num = int(input())
init_changeable_num = init_num

round = 0

while True:
    round += 1
    if init_changeable_num < 10:
        next_num = init_changeable_num*10 + init_changeable_num
    else:
        r_num = init_changeable_num%10
        out_num = init_changeable_num//10 + r_num
        next_num = r_num*10 + out_num%10
    
    if (init_num == next_num): break
    init_changeable_num = next_num

print(round)