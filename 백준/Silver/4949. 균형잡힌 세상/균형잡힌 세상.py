import sys
input = sys.stdin.readline

INDEX_PARENTHESES = 0
INDEX_CURLY_BRACKETS = 1
INDEX_OF_BRACKET_START = 0
INDEX_OF_BRACKET_END = 1
bracket_group = [('(', '['), (')', ']')]

while (input_str := input().rstrip()) != '.':
    temp_storage = []
    for character in input_str:
        if character in bracket_group[INDEX_OF_BRACKET_START]:
            temp_storage.append(character)
        elif character in bracket_group[INDEX_OF_BRACKET_END]:
            try:
                if bracket_group[INDEX_OF_BRACKET_START].index(temp_storage[-1]) == bracket_group[INDEX_OF_BRACKET_END].index(character):
                    temp_storage.pop()
                else:
                    print('no')
                    break
            except IndexError:
                print('no')
                break
    else:
        if len(temp_storage) == 0:
            print('yes')
        else:
            print('no')