'''
# 기타줄
Day Of Mourning의 기타리스트 강토가 사용하는 기타에서 N개의 줄이 끊어졌다. 따라서 새로운 줄을 사거나 교체해야 한다. 
강토는 되도록이면 돈을 적게 쓰려고 한다. 6줄 패키지를 살 수도 있고, 1개 또는 그 이상의 줄을 낱개로 살 수도 있다.

끊어진 기타줄의 개수 N과 기타줄 브랜드 M개가 주어지고, 각각의 브랜드에서 파는 기타줄 6개가 들어있는 패키지의 가격, 낱개로 살 때의 가격이 주어질 때, 
적어도 N개를 사기 위해 필요한 돈의 수를 최소로 하는 프로그램을 작성하시오.

[입력]
첫째 줄에 N과 M이 주어진다. N은 100보다 작거나 같은 자연수이고, M은 50보다 작거나 같은 자연수이다. 
둘째 줄부터 M개의 줄에는 각 브랜드의 패키지 가격과 낱개의 가격이 공백으로 구분하여 주어진다. 가격은 0보다 크거나 같고, 1,000보다 작거나 같은 정수이다.

[출력]
첫째 줄에 기타줄을 적어도 N개 사기 위해 필요한 돈의 최솟값을 출력한다.

[예제 입력]
4 2
12 3
15 4

[예제 출력]
12

'''
import math
import heapq

N, M = map(int, input().split())
price_list = []
package_price_group = []
each_price_group = []

for _ in range(M):
    package_price, each_price = map(int, input().split())
    heapq.heappush(package_price_group, package_price)
    heapq.heappush(each_price_group, each_price)

min_package_price = heapq.heappop(package_price_group)
min_each_price = heapq.heappop(each_price_group)
total_price = 0

if min_package_price < min_each_price*6:
    amount_package = 1 if N // 6 == 0 else math.ceil(N // 6)
    total_price += amount_package * min_package_price
    
    left_amount_strings = N-(amount_package*6)
    if left_amount_strings*min_each_price < min_package_price:
        total_price += left_amount_strings * min_each_price if left_amount_strings > 0 else 0
    else:
        total_price += min_package_price
else:
    total_price += N * min_each_price
print(total_price)
