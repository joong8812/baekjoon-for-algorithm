from collections import deque
import sys

def getQueueCommandResult(command, my_queue):
    NO_VALUE = -1
    EMPTY = 1
    NO_EMPTY = 0
    
    if 'push' in command:
        val = command.split(' ')[1]
        my_queue.append(val)
    elif 'pop' in command:
        print(my_queue.popleft() if len(my_queue) > 0 else NO_VALUE)
    elif 'size' in command:
        print(len(my_queue))
    elif 'empty' in command:
        print(NO_EMPTY if len(my_queue) > 0 else EMPTY)
    elif 'front' in command:
        print(my_queue[0] if len(my_queue) > 0 else NO_VALUE)
    elif 'back' in command:
        print(my_queue[-1] if len(my_queue) > 0 else NO_VALUE)
        
input = sys.stdin.readline

n = int(input())
my_queue = deque() 

for _ in range(n):
    getQueueCommandResult(input().strip(), my_queue)