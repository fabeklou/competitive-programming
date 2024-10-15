t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())
    s1 = input()
    s2 = input()

    arr1 = sorted(list(s1))
    arr2 = sorted(list(s2))
    result = []

    i, j = 0, 0
    turn = True if arr1[i] < arr2[j] else False
    count = 0

    while i < n and j < m:
        if turn:
            prev = arr1[i]
            result.append(arr1[i])
            i += 1
            for _ in range(k-1):
                if i < n and arr1[i] == prev:
                    result.append(arr1[i])
                    i += 1
                else:
                    break
        else:
            prev = arr2[j]
            result.append(arr2[j])
            j += 1
            for _ in range(k-1):
                if j < m and arr1[j] == prev:
                    result.append(arr2[j])
                    j += 1
                else:
                    break
        turn = False if turn else True

    print("".join(result))
