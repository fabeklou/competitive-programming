from collections import deque

for _ in range(int(input())):
    n = int(input())
    a = deque(sorted(map(int, input().split())))
    while len(a) > 1:
        if a[1] - a[0] <= 1:
            a.popleft()
        else:
            break
    print('YES' if len(a) == 1 else 'NO')
