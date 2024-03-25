from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))

L = good = 0
count = defaultdict(int)

for R in range(n):
    count[arr[R]] += 1
    while count[arr[R]] == k:
        good += len(arr) - R
        count[arr[L]] -= 1
        L += 1

print(good)
