from collections import Counter

s = input()
m = int(input())

queries = [tuple(map(int, input().strip().split())) for _ in range(m)]

n = len(s)
cons_count = [0] * n
cons_count[0] = 0
for i in range(1, n):
    if s[i] == s[i - 1]:
        cons_count[i] = cons_count[i - 1] + 1
    else:
        cons_count[i] = cons_count[i - 1]
        
print([i for i in range(1,n+1)])        
print(cons_count)

for li, ri in queries:
    if li == 1:
        print(cons_count[ri - 1])
    else:
        print(cons_count[ri - 1] - cons_count[li - 1])
