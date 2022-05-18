number_group = input().split('-')

organized_number_group = []
for i, num in enumerate(number_group):
  if i == 0 and '+' in num:
    organized_number_group.append(sum(list(map(int, num.split('+')))))
  elif i == 0:
    organized_number_group.append(int(num))
  else:
    organized_number_group.append(sum(list(map(int, num.split('+')))) * -1)

print(sum(organized_number_group))