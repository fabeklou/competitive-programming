n = int(input())
arr = list(map(int, input().split()))

odd = even = False
for num in arr:
    if num % 2 == 1:
        odd = True
    else:
        even = True

if odd and even:
    arr.sort()
print(*arr)
