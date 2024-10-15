from collections import defaultdict

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

sm = 0
count = 0
for num in nums:
    if num >= sm:
        count += 1
        sm += num

print(count)
