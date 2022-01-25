s1 = "aaabbaaa"
s2 = "wowwow"


def make_circle_string(s):
    string_circle = ""
    for i, letter in enumerate(s):
        if i == 0:
            first_letter = letter
            string_circle = letter
        elif letter is not first_letter:
            string_circle = s[i:] + s[:i]
            break
    return string_circle


def solution(s):
    string_line = s
    string_circle = make_circle_string(string_line)

    letter_count_list = []
    count = 0
    for i, letter in enumerate(string_circle):
        if i == 0:
            standard_letter = letter
        elif standard_letter is not letter:
            letter_count_list.append(count)
            standard_letter = letter
            count = 0

        count += 1

        if i == len(string_circle) - 1:
            letter_count_list.append(count)

    print(sorted(letter_count_list))

solution(s1)


