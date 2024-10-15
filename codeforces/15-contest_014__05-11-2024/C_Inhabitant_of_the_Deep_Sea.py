import math

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    left, right = 0, n-1
    count = 0

    # 4 5
    # 1 2 4 3
    while left <= right and k > 0:

        if left == right:
            count += 1 if arr[left] <= k else 0
            break

        hits = min(arr[left], arr[right], k // 2 + k % 2)

        arr[left] -= hits
        k -= hits
        if k > 0:
            arr[right] -= hits
            k -= hits

        if arr[left] == 0:
            left += 1
            count += 1
        if arr[right] == 0:
            right -= 1
            count += 1

    print(count)
