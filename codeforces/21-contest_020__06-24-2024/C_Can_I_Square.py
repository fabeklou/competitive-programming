import math

for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))

    list_sum = sum(lst)
    sqrt_sum = int(math.sqrt(list_sum))

    if sqrt_sum ** 2 == list_sum:
        print("YES")
    else:
        print("NO")
