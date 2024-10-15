import sys
ipt = sys.stdin.readline

t = int(ipt())

for _ in range(t):
    n, m = map(int, ipt().split())
    arr1 = list(map(int, ipt().split()))
    arr2 = list(map(int, ipt().split()))

    arr1.sort()
    arr2.sort(reverse=True)

    size1 = len(arr1)
    size2 = len(arr2)
    i, j = 0, size1-1
    a, b = 0, size2-1
    max_iter = min(size1, size2)
    max_diff = 0

    while max_iter:
        left = abs(arr1[i] - arr2[a])
        right = abs(arr1[j] - arr2[b])

        if max_iter == 0:
            max_diff += max(left, right)
            break

        if left > right:
            max_diff += left
            i += 1
            a += 1
        else:
            j -= 1
            b -= 1
            max_diff += right

        max_iter -= 1

    print(max_diff)
