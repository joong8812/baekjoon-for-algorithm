def get_minimum_move(start, goal):
    distance = goal - start
    group_boundary = 2
    current_group = 1
    while True:
        if distance <= group_boundary:
            break
        current_group += 1
        group_boundary = group_boundary + (2 * current_group)
    middle_boundary_of_group = group_boundary - current_group
    estimate_min_move = 2*(current_group)
    return estimate_min_move-1 if distance <= middle_boundary_of_group else estimate_min_move

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    print(get_minimum_move(x, y))