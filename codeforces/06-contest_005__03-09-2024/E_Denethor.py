import sys
ipt = sys.stdin.readline

t = int(ipt())

for _ in range(t):
    n = int(ipt())
    arr1 = list(map(int, ipt().split()))
    arr2 = list(map(int, ipt().split()))

    count = len(arr1)
    top, bottom = len(arr1) - 1, len(arr2) - 1

    while top >= 0 and bottom >= 0:
        if arr1[top] == arr2[bottom]:
            count -= 1
            top -= 1
            bottom -= 1
        else:
            top -= 1

    print(count)
