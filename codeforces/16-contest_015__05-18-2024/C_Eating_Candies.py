for _ in range(int(input())):

    n = int(input())
    w = list(map(int, input().split()))

    left, right = -1, n
    LW = RW = count = 0
    result = -1

    """
    2  1  4  2  4  1
    1 2 4 8 16
    7 3 20 5 15 1 11 8 10
    """

    while left < right:
        if LW == RW:
            result = max(result, count)
            left += 1
            right -= 1
            LW += w[left]
            RW += w[right]
            count+=2
        elif LW < RW:
            left += 1
            LW += w[left]
            count+=1
        else:
            right -= 1
            RW += w[right]
            count+=1

    print(result if result != -1 else 0)
    