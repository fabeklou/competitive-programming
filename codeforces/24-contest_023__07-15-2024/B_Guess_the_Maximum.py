for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    maxi = float('+inf')
    for index in range(n-1):
        maxi = min(maxi, max(arr[index], arr[index + 1]))
    print(maxi - 1)
