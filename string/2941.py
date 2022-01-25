# def count_word_in_the_string(word):
#     croatia_words = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
#     count = 0
#
#     if not word.strip():
#         return count
#
#     for char in croatia_words:
#         pos = word.find(char)
#         if pos > -1:
#             word = word.replace(char, " ", 1)
#             count += 1
#             break
#
#     left_characters = word.strip()
#     if count == 0 and len(left_characters):
#         left_characters = left_characters.replace(" ", "")
#         count += len(left_characters)
#         word = ""
#
#     return count_word_in_the_string(word) + count
#
#
# input_word = input()
# print(count_word_in_the_string(input_word))

croatia_words = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
input_word = input()

for word in croatia_words:
    input_word = input_word.replace(word, "!")

print(len(input_word))

