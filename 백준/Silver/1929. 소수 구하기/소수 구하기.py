def get_prime_numbers(end):
    all_numbers = [True] * (end+1)
    all_numbers[0] = False
    all_numbers[1] = False
    
    for num in range(2, end+1):
        if all_numbers[num] == True:
            variable_num = 2
            while num*variable_num <= end:
                all_numbers[num*variable_num] = False
                variable_num += 1
    prime_numbers = []
    for num, is_prime in enumerate(all_numbers):
        if is_prime:
            prime_numbers.append(num)
    return prime_numbers
    
start, end = map(int, input().split())
for prime_number in get_prime_numbers(end):
    if prime_number >= start:
        print(prime_number)