round = int(input())

while round > 0:
    a_class = list(map(int, input().split()))
    student_num = a_class[0]
    list_score = a_class[1:]

    avg_score = sum(list_score) / student_num
    count_over_avr = len([x for x in list_score if x > avg_score])

    result = count_over_avr/student_num * 100
    print("%0.3f" % result + "%")
    
    round -= 1

