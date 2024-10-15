import sys

n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    nodeA, nodeB = map(int, input().split())
    graph[nodeA-1].append(nodeB-1)
    graph[nodeB-1].append(nodeA-1)

# check for star topology
center = 0
others = 0
for nodes in graph:
    if len(nodes) == n - 1:
        center += 1
    if len(nodes) == 1:
        others += 1
if center == 1 and others == n - 1:
    print("star topology")
    sys.exit()
    

# check for ring topology
if all([len(nodes) == 2 for nodes in graph]):
    print("ring topology")
    sys.exit()

# check for bus topology
ones = 0
twos = 0
for nodes in graph:
    if len(nodes) == 1:
        ones += 1
    elif len(nodes) == 2:
        twos += 1
if ones == 2 and twos == n - 2:
    print("bus topology")
    sys.exit()

# if unknown
print("unknown topology")
