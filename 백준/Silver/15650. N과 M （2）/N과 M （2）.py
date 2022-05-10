import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sequence_list = []
visited = [False] * (n+1)

def dfs(node):
  if len(sequence_list) == m:
    print(*sequence_list)
    return
  
  for i in range(node+1, n+1):
    visited[i] = True
    sequence_list.append(i)
    dfs(i)
    sequence_list.pop()
    visited[i] = False
    
dfs(0)