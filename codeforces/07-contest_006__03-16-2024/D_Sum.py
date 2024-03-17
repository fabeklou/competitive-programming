t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    arr.sort()
    sm = sum(arr)
    left = 0
    right = n - 1
    
    for i in range(k):
        if left < n - 2 and sm - (arr[left] + arr[left+1]) > sm - arr[n-1]:
            left += 2
            sm -= (arr[left] + arr[left+1])
        else:
            right -= 1
            sm -= arr[right]
    print(sum(arr[left:right+1]))
