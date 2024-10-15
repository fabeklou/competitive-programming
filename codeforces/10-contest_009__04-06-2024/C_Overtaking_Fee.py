from collections import defaultdict
import copy

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

prefixA=defaultdict(set)
prefixB=defaultdict(set)
curr1,curr2 = set(),set()
for i in range(n):
    prefixA[a[i]] = copy.deepcopy(curr1)
    curr1.add(a[i])
    prefixB[b[i]] = copy.deepcopy(curr2)
    curr2.add(b[i])
count=0
curr1.clear()
curr2.clear()
for num in a:
    if prefixA[num] & prefixB[num]:
        continue
    count+=1

print(count)
