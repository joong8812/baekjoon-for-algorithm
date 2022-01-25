input_num = int(input())

count = 0
for num in range(1, input_num+1):
    place_len = len(str(num))
    value_list = []
    diff = 0
    
    if place_len < 3:
        count += 1
    else:
        for place_value in range(place_len):
            value_list.append((num // 10 ** place_value) % 10)
        for n in range(place_len-1):
            if n == 0:
                diff = value_list[n] - value_list[n+1]
            else:
                if diff is not value_list[n] - value_list[n+1]:
                    break
        else:
            count += 1

print(count)
