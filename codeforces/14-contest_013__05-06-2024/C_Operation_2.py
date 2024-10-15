from collections import deque

a, b = map(int, input().split())

dq = deque([(a, 0)])
visited = set()
visited.add(a)
found=False

while dq:
    num, ops = dq.popleft()

    if num == b:
        print(ops)
        found=True
        break

    multi = num * 2
    sub = num - 1

    if multi not in visited and multi <= b * 2:
        dq.append((multi, ops + 1))
        visited.add(multi)
    if sub > 0 and sub not in visited:
        dq.append((sub, ops + 1))
        visited.add(sub)

if not found: print(-1)
