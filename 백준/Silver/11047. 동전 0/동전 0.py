n, k = map(int, input().split())
coin_list = []
count = 0
while count < n:
    coin_list.append(int(input()))
    count += 1
coin_list.sort(reverse=True)

coin_amounts = 0
for price in coin_list:
    need_amount = k // price
    if need_amount > 0:
        coin_amounts += need_amount
        k -= price * need_amount
        if k == 0:
            break
print(coin_amounts)