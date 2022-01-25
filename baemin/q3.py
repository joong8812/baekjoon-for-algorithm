

def total_ings_price(all_ings, ings):
    total = 0
    for ing in all_ings:
        total += ings[ing]
    return total

def solution(ings, menu, sell):
    dict_ings = {}
    dict_menu = {}

    # 재료 list -> 재료 dictionary
    for item in ings:
        temp_list = item.split()
        dict_ings[temp_list[0]] = int(temp_list[1])

    # 메뉴 list -> 메뉴 dictionary
    for item in menu:
        temp_list = item.split()
        dict_menu[temp_list[0]] = [temp_list[1], int(temp_list[2])]

    total_sell = 0
    # 판매 실적 계산
    for item in sell:
        temp_list = item.split()
        menu = temp_list[0]
        amount = int(temp_list[1])
        total_sell += (dict_menu[menu][1] - total_ings_price(dict_menu[menu][0], dict_ings)) * amount
        
    return total_sell

# testcase_1
ings = ["r 10", "a 23", "t 124", "k 9"]	
menu = ["PIZZA arraak 145", "HAMBURGER tkar 180", "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45", "JUICE rra 55", "WATER a 20"]	
sell = ["BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"]	
#result: 1161
# testcase_2
# ings = ["x 25", "y 20", "z 1000"]
# menu = ["AAAA xyxy 15", "TTT yy 30", "BBBB xx 30"]
# sell = ["BBBB 3", "TTT 2"]
#result: -80
print(solution(ings, menu, sell))
    
