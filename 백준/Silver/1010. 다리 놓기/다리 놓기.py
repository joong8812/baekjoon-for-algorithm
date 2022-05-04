t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    if m > n: n,m = m,n
    parent_num = 1
    for num in range(n-m+1, n+1):
        parent_num *= num
        
    child_num = 1
    for num in range(1, m+1):
        child_num *= num
    print(parent_num // child_num)