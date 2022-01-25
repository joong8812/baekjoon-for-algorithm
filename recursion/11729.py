top_level = int(input())


def hanoi(number_of_disks_to_move, from_, to_, via_):
    if number_of_disks_to_move == 1:
        print(from_, to_)
    else:
        hanoi(number_of_disks_to_move-1, from_, via_, to_)
        print(from_, to_)
        hanoi(number_of_disks_to_move-1, via_, to_, from_)

print(str(2**top_level - 1))
hanoi(top_level, "1", "3", "2")

# https://ko.wikipedia.org/wiki/%ED%95%98%EB%85%B8%EC%9D%B4%EC%9D%98_%ED%83%91
# https://st-lab.tistory.com/96