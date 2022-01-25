total_testcase = int(input())

for i in range(total_testcase):
    A, B = map(int, input().split())
    print(f"Case #{i+1}: {A+B}")