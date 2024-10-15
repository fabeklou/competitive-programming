from collections import deque

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if sum(a) / len(a) == a[0]:
        print('NO')
    else:
        dq = deque(sorted(a))
        sm = 0
        b = []
        while dq:
            if sm != dq[0]:
                b.append(dq.popleft())
                sm += b[-1]
            elif sm != dq[-1]:
                b.append(dq.pop())
                sm += b[-1]
            else:
                b.append(dq.pop())
                b[0], b[-1] = b[-1], b[0]
                sm += b[0]

        print('YES')
        print(*b)
