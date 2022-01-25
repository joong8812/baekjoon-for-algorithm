input_string = input().lower()
count_char_list = [0 for _ in range(26)]

for char in input_string:
    count_char_list[ord(char) - ord('a')] += 1

max_count = max(count_char_list)
max_index_list = []

for idx, count in enumerate(count_char_list):
    if max_count == count:
        max_index_list.append(idx)

print("?" if len(max_index_list) > 1 else chr(max_index_list[0] + ord('a')).upper())