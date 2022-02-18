'''
[잃어버린 괄호]
세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.
그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.
괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

[입력]
첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다. 
그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다. 수는 0으로 시작할 수 있다. 
입력으로 주어지는 식의 길이는 50보다 작거나 같다.

[예제입력]
55-50+40

[예제출력]
-35
'''
f = input()
divide_by_minus = f.split('-')
firstnum = divide_by_minus.pop(0)
total_negative_num = 0
total_positive_num = 0

for each_part in divide_by_minus:
    nums = list(map(int, each_part.split('+')))
    total_negative_num += sum(nums)

if firstnum != 0:
    nums = list(map(int, firstnum.split('+')))
    total_positive_num += sum(nums)

min_num = total_positive_num - total_negative_num
print(min_num)