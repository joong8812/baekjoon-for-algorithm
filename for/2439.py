total_rows = int(input())

for row in range(total_rows):
    a_row = ""
    for col in range(total_rows):
        a_row += '*' if col >= (total_rows-1)-row else " "
    print(a_row)