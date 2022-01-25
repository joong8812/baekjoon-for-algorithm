# grid1 = ['1','234','56789']
# grid2 = ['a','man','drink','water11']
# def solution3(grid, clockwise):
#     if clockwise:
#         return clockwise1(grid)
#     else:
#         return clockwise1(clockwise1(grid))
# def clockwise1(grid):
#     leng = len(grid)
#     changed_arr = ['' for _ in range(leng)]
#     for i,g in enumerate(grid):
#         #gridarr = list(g)
#         gridarr = g
#         #print(gridarr)
#         for idx,char in enumerate(gridarr):
#             place = leng - 1 - i + ((idx+1)//2)
#             changed_arr[place] = char + changed_arr[place]
#             print(changed_arr)
#     return changed_arr
# print(solution3(grid1, True))
# print(solution3(grid2, False))

input = ['1', '234', '56789']

input_size = len(input)
output_list = ['' for _ in range(input_size)]

for input_index, set_numbers in enumerate(input):
    for char_index_in_current_string, char in enumerate(set_numbers):
        pos = input_size - 1 - input_index + ((char_index_in_current_string+1)//2)
        output_list[pos] = char + output_list[pos]
print(output_list)