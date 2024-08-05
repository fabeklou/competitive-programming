# Problem: D - Chat Screenshots - https://codeforces.com/gym/540348/problem/D

from collections import deque

for _ in range(int(input())):
    n, k = map(int, input().split())
    graph = [[] for _ in range(n)]
    visited_edges = set()
    
    # build the directed graph
    for _ in range(k):
        relations = list(map(int, input().split()))
        for index in range(1, len(relations) - 1):
            if (relations[index] - 1, relations[index + 1] - 1) not in visited_edges:
                graph[relations[index] - 1].append(relations[index + 1] - 1)
                visited_edges.add((relations[index] - 1, relations[index + 1] - 1))

    dq = deque()
    incoming = [0] * n
    
    for node in range(n):
        for neighbor in graph[node]:
            incoming[neighbor] += 1

    for node, count in enumerate(incoming):
        if count == 0:
            dq.append(node)

    result = []
    while dq:
        node = dq.popleft()
        result.append(node)
        for neighbor in graph[node]:
            incoming[neighbor] -= 1
            if incoming[neighbor] == 0:
                dq.append(neighbor)

    print('YES' if len(result) == n else 'NO')
