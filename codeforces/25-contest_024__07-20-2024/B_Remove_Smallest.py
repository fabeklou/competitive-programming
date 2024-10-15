from collections import deque

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    dq = deque(arr)

    while len(dq) > 1 and dq[1] - dq[0] <= 1:
        dq.popleft()
    
    if len(dq) == 1:
        print("YES")
    else:
        print('NO')
