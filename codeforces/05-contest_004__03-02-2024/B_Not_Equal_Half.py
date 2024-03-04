n = int(input())

arr = list(map(int, input().split()))
arr.sort()

print(-1) if arr[0] == arr[-1] else print(*arr)
