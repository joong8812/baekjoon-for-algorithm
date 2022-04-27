import sys
input = sys.stdin.readline
n = int(input())
coordinate_group = []
for _ in range(n):
    coordinate_group.append(tuple(map(int, input().split())))
coordinate_group.sort(key=lambda x: (x[1], x[0]))
for coordinate in coordinate_group:
    
    print(coordinate[0], coordinate[1])