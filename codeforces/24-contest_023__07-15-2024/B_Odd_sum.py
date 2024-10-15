n = int(input())
arr = list(map(int, input().split()))

positive_sum = 0
max_negative_odd = float('-inf')
min_positive_odd = float('+inf')

for num in arr:
    if num > 0:
        positive_sum += num
    if num > 0 and num % 2:
        min_positive_odd = min(min_positive_odd, num)
    if num < 0 and num % 2:
        max_negative_odd = max(max_negative_odd, num)

if positive_sum % 2:
    print(positive_sum)
else:
    optimal_sub = min(min_positive_odd, -max_negative_odd)
    print(positive_sum - optimal_sub)
