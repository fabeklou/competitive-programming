import math

t = int(input())

# it is necessary to apply modulo each time you make a modif

for _ in range(t):
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    arr1.sort()
    arr2.sort()
    
    count = 0
    de = 0
    p1 = 1
    p2 = 1

    for i in range(n):
        if arr1[i] > arr2[i]:
            count += 1
        else:
            de += 1
        p1 *= arr1[i]
        p2 *= arr2[i]
    if de > 0:
        print(0)
    else:
        print(p1 // p2)
        # print(int(math.pow(2, count + de)))
