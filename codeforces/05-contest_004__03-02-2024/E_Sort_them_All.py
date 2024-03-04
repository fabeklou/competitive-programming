import sys

t = int(sys.stdin.readline())


def sortBoth(arr1, arr2, size):
    count = 0
    for i in range(size - 1):
        k = i
        for j in range(i+1, size):
            if arr1[j] < arr1[k]:
                k = j
        if not i is k:
            swaps.append((k+1, i+1))
            arr1[i], arr1[k] = arr1[k], arr1[i]
            arr2[i], arr2[k] = arr2[k], arr2[i]
            count += 1
    return count


for _ in range(t):
    size = int(sys.stdin.readline())
    arr1 = list(map(int, sys.stdin.readline().split()))
    arr2 = list(map(int, sys.stdin.readline().split()))

    swaps = []
    count = 0

    # using selection sort to sort a arr1 based on arr2
    count += sortBoth(arr1, arr2, size)

    # check if both arrays are sorted
    if arr2 != sorted(arr2):
        count += sortBoth(arr2, arr1, size)
    else:
        print(count)
        for x, y in swaps:
            print(x, y)
        break

    if arr2 == sorted(arr2):
        print(count)
        for x, y in swaps:
            print(x, y)
    else:
        print(-1)
