test_case = [["홍콩", "11PM", "9AM"], ["엘에이", "3PM", "2PM"]]

def solution(time, plans):
    friday_checkout_time = 18
    monday_checkin_time = 13
    travel_country = []

    for plan in plans:
        depart_time = int(plan[1][:-2])
        need_time_for_friday = (depart_time + (12 if plan[1].find("PM") > 0 else 0)) - friday_checkout_time

        arrive_time = int(plan[2][:-2])
        need_time_for_monday = monday_checkin_time - (arrive_time + (12 if plan[2].find("PM") > 0 else 0))

        if time + (need_time_for_friday + need_time_for_monday) >= 0:
            travel_country.append(plan[0])
    return travel_country


print(solution(3.5, test_case))

# 12:00 P.M 경우
# 금요일에 일찍 출발 하는 경우