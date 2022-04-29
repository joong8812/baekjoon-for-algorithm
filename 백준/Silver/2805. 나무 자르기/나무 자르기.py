import sys
input = sys.stdin.readline
n, m = map(int, input().split())
trees = list(map(int, input().split()))

cutter_height = 0
start = 0
end = max(trees)

while start <= end:
    amount_tree = 0
    middle = (start + end) // 2
    amount_tree = sum(tree-middle if tree > middle else 0 for tree in trees)
    
    if amount_tree >= m:
        cutter_height = middle
        start = middle + 1
    else:
        end = middle - 1
print(cutter_height)