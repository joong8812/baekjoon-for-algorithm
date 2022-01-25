import sys

while case := sys.stdin.readline():
    a, b = map(int, case.split())
    print(a+b)



input_cases = sys.stdin.readlines()
print(input_cases)

for case in input_cases:
    a, b = map(int, case.split())
    print(a+b)

# while True:
#     try:
#         a, b = map(int, input().split())
#         print(a+b)
#     except EOFError:
#         break

print('Exit while statement')