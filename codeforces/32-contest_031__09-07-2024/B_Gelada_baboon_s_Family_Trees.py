n = int(input())
p = list(map(int, input().split()))

root = list(range(n))
size = [1] * n


def find(v):
    if v == root[v]:
        return v
    root[v] = find(root[v])
    return root[v]


def union(v1, v2):
    root1, root2 = find(v1), find(v2)
    if root1 == root2:
        return
    if size[root1] > size[root2]:
        root[root2] = root1
        size[root1] += size[root2]
    else:
        root[root1] = root2
        size[root2] += size[root1]


for i in range(n):
    v = i
    while v != root[v]:
        root[v] = root[root[v]]
        v = root[v]
    root_i = v

    v = p[i] - 1
    while v != root[v]:
        root[v] = root[root[v]]
        v = root[v]
    root_p = v

    if root_i != root_p:
        if size[root_i] > size[root_p]:
            root[root_p] = root_i
            size[root_i] += size[root_p]
        else:
            root[root_i] = root_p
            size[root_p] += size[root_i]

distinct_roots = len(set(find(i) for i in range(n)))
print(distinct_roots)
