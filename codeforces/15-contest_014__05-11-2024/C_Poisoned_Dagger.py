for _ in range(int(input())):
    n, h = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    left, right = 1, h
    res = float('+inf')

    while left <= right:
        mid = left + (right - left)//2
        total = 0
        for i in range(n):
            if i < n-1:
                curr = min(mid, a[i+1] - a[i])
            else:
                curr = mid
            total += curr
        # print('->', mid, total)
        if total > h:
            right = mid - 1
            res = min(res, mid)
        elif total < h:
            left = mid + 1
        else:
            res = mid
            break

    print(res)
