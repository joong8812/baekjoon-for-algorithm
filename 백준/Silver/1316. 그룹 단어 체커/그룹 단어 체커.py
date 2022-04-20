n = int(input())
group_word_count = 0

for _ in range(n):
    word = input()
    prev_c = ""
    used_c = []
    for curr_c in word:
        if prev_c != curr_c:
            try:
                used_c.index(curr_c)
                break
            except ValueError:
                used_c.append(curr_c)
        prev_c = curr_c
    else:
        group_word_count += 1
print(group_word_count)