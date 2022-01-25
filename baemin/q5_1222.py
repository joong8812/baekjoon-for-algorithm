
def solution(rows, columns):
    num_map = []
    for _ in range(rows):
        num_map.append([0]*columns)

    r = 0
    c = 0
    num_count = 1
    while True:
        num_map[r][c] = num_count
        if num_count % 2 == 1:
            if c < columns-1:
                c += 1
            else:
                c = 0
        else:
            if r < rows-1:
                r += 1
            else:
                r = 0

        if rows == columns:
            if num_count == 2*rows:
                break
        if all(0 not in rlist for rlist in num_map):
            break

        num_count += 1
    return num_map

print(solution(3, 4))
print(solution(3, 3))