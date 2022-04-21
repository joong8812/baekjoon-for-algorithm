weight_five, weight_three = 5, 3
n = int(input())

possible_case = []
five_kg_bag = 0
while weight_five * five_kg_bag <= n:
    left_weight = n - (weight_five * five_kg_bag)
    three_kg_bag = left_weight // weight_three
    if n == (five_kg_bag*weight_five + three_kg_bag*weight_three):
        possible_case.append(five_kg_bag+three_kg_bag)
    five_kg_bag += 1

print(-1 if len(possible_case) == 0 else min(possible_case))