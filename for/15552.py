import sys

total_testcase = int(sys.stdin.readline().rstrip())
testcase_list = []

# 입력
for i in range(total_testcase):
    testcase_list.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 출력
for testcase in testcase_list:
    print(f"{testcase[0] + testcase[1]}")

# ######################################################
total_testcase = int(input())

for _ in range(total_testcase):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)