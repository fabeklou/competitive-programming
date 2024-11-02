# Problem: c - Reposts - https://codeforces.com/gym/533316/problem/c

from collections import defaultdict

n = int(input())
graph = defaultdict(list)
for _ in range(n):
    name1, _, name2 = input().split()
    name1, name2 = name1.lower(), name2.lower()
    graph[name2].append(name1)

def dfs(node):
    max_length = 1
    for neighbor in graph[node]:
        max_length = max(max_length, 1 + dfs(neighbor))
    return max_length

result = dfs('polycarp')
print(result)
