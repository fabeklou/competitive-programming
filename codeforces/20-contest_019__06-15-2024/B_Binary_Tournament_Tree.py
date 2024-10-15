def rec_depth(arr, depth, map):
    if not arr:
        return

    maxi, maxiIdx = 0, 0
    for i in range(len(arr)):
        if arr[i] > maxi:
            maxi = arr[i]
            maxiIdx = i
    
    map[maxi] = depth
    rec_depth(arr[:maxiIdx], depth+1, map)
    rec_depth(arr[maxiIdx+1:], depth+1, map)


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    hMap = {}
    
    rec_depth(arr, 0, hMap)
    
    print(*[ hMap[num] for num in arr ])
