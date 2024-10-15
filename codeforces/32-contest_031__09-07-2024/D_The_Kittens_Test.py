from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dq = deque()
for node in graph:
    if len(node) == 1:
        dq.append(node[0])
        break

visited = set()
order = []
while dq:
    node = dq.popleft()
    order.append(node)
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dq.append(neighbor)

print(*order)
