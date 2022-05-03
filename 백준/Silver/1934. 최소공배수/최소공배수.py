import sys

def GCD(x, y):
    while(y):
        x,y = y, x%y
    return x

def LCM(x, y):
    return x*y // GCD(x,y)

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    
    print(LCM(a,b))