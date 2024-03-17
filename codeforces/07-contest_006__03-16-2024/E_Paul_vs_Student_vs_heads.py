import sys

ipt = sys.stdin.readline

n = int(ipt())
arr1 = list(map(int, ipt().split()))
m = int(input())
arr2 = list(map(int, ipt().split()))

sum1 = sum(arr1)
sum2 = sum(arr2)

arr1.sort()
arr2.sort()

if sum1 == sum2:
    left1, left2 = 0, 0
    right1, right2 = n-1, m-1
    count = 0
    
    while left1 <= right1 and left2 <= right2:
        if arr1[left1] == arr2[left2]:
            left1 += 1
            left2 += 1
            count += 1       
        elif arr1[right1] == arr2[right2]:
            right1 -= 1
            right2 -= 1
            count += 1
        if arr1[right1] != arr2[right2] and arr1[left1] != arr2[left2]:
            count += 1
            break
    
    print(count)  
        
else:
    print(-1)
