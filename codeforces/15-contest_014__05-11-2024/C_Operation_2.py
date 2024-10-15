from collections import deque

a, b = map(int, input().split())

def find_min_ops(origin, target):
    dq = deque([(origin, 0)])
    visited = set()

    while dq:
        pos, ops = dq.popleft()
        
        if pos == target:
            return ops

        mul = pos * 2
        sub = pos - 1
        
        if mul not in visited and mul <= target*2:
            visited.add(mul)
            dq.append((mul, ops+1))
        if sub not in visited and sub > 0:
            visited.add(sub)
            dq.append((sub, ops+1))

print(find_min_ops(a, b))
