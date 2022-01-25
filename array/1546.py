n = int(input())
subjects = list(map(int, input().split()))

m = max(subjects)
new_total = 0

for score in subjects:
    new_total += score/m * 100
    
print(new_total/n)
