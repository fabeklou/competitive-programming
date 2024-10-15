import math

for _ in range(int(input())):
    n =  int(input())
    arr = list(map(int, input().split()))
    
    side = int(math.sqrt(sum(arr)))
    
    if side ** 2 != sum(arr):
        print("NO")
    else:
        print("YES")
