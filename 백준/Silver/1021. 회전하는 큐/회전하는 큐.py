import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def pop_num(rotate_queue):
    rotate_queue.pop(0)
    return rotate_queue

def move_to_left(rotate_queue):
    for index in range(len(rotate_queue)-1):
        rotate_queue[index], rotate_queue[index+1] = rotate_queue[index+1], rotate_queue[index]
    return rotate_queue

def move_to_right(rotate_queue):
    for index in range(len(rotate_queue)-1, 0, -1):
        rotate_queue[index], rotate_queue[index-1] = rotate_queue[index-1], rotate_queue[index]
    return rotate_queue

rotate_queue = [n for n in range(1, N+1)]
pop_num_list = list(map(int, input().split()))
operate_count = 0
for target_num in pop_num_list:
    move_left = False
    
    if rotate_queue.index(target_num) <= (len(rotate_queue) // 2):
        move_left = True
    
    while target_num != rotate_queue[0]:
        if move_left:
            rotate_queue = move_to_left(rotate_queue)
        else:
            rotate_queue = move_to_right(rotate_queue)
        operate_count += 1
        
    rotate_queue = pop_num(rotate_queue)
print(operate_count)