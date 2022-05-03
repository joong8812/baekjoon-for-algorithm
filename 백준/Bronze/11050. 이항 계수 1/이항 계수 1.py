n,k = map(int, input().split())
parent_num = 1
for num in range(n-k+1, n+1):
    parent_num *= num
    
child_num = 1
for num in range(1, k+1):
    child_num *= num
print(parent_num // child_num)