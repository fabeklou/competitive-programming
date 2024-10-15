from collections import defaultdict, Counter

for _ in range(int(input())):
    vs, es = map(int, input().split())
    
    graph = [0] * (vs+1)
    for _ in range(es):
        u, v = map(int, input().split())
        graph[u] += 1
        graph[v] += 1

    count  = Counter(graph)
    x, y = 0, 0
    for key in count.keys():
        if key > 1 and count[key] > 1:
            y = count[key] - 1
        if key > 1 and count[key] == 1:
            x = count[key]

    if x == 0:
        
    else: