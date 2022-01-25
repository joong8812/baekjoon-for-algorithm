def solution(arr):
    # 입력 리스트 안 1,2,3 별로 카운트 하여 그 수를 리스트에 담는다
    count_list = []
    for num in range(1, 4):
        count_list.append(arr.count(num))

    # 가장 많은 수의 개수를 구한다
    max_val = max(count_list)
    
    # 가장 많은 개수 - 각 값의 개수 = 추가 해야 할 개수
    return list(map(lambda x: max_val-x, count_list))


ex1_list = [2, 1, 3, 1, 2, 1]
ex2_list = [3, 3, 3, 3, 3, 3]
ex3_list = [1, 2, 3]
print(solution(ex1_list))
print(solution(ex2_list))
print(solution(ex3_list))