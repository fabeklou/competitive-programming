from collections import defaultdict

n, k  = map(int, input().split())
arr = list(map(int, input().split()))

L = 0
target = total = 0
count = defaultdict(int)

for R in range(n):
    if arr[R] not in count:
        target += 1
    count[arr[R]] += 1

    while target > k:
        count[arr[L]] -= 1
        if count[arr[L]] == 0:
            target -= 1
            del count[arr[L]]
        L += 1

    total += R-L+1

print(total)
        