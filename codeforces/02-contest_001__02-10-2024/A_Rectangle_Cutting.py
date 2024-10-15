t = int(input())

for _ in range(t):
    a, b = [int(num) for num in input().split()]
    if a % 2 == 0 and a / 2 != b:
        print('Yes')
    elif b % 2 == 0 and b / 2 != a:
        print('Yes')
    else:
        print('No')
