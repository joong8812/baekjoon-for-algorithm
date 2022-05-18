f = input()
divide_by_minus = f.split('-')
firstnum = divide_by_minus.pop(0)
total_negative_num = 0
total_positive_num = 0

for each_part in divide_by_minus:
    nums = list(map(int, each_part.split('+')))
    total_negative_num += sum(nums)

if firstnum != 0:
    nums = list(map(int, firstnum.split('+')))
    total_positive_num += sum(nums)

min_num = total_positive_num - total_negative_num
print(min_num)