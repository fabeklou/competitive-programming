from collections import deque

nodes, max_cons = map(int, input().split())
path = [0] + list(map(int, input().split()))

graph = [[] for _ in range(nodes + 1)]
for _ in range(nodes - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
dq = deque([(1, path[1], -1)])

while dq:
    v, cats, parent = dq.popleft()

    if cats > max_cons:
        continue

    for u in graph[v]:
        if u == parent:
            continue
        if path[u] == 1:
            dq.append((u, cats + 1, v))
        else:
            dq.append((u, 0, v))

    if len(graph[v]) == 1 and v != 1:
        count += 1

print(count)
