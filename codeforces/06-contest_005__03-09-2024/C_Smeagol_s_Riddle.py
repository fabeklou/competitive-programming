import sys
from collections import Counter
ipt = sys.stdin.readline

n = int(ipt())

for _ in range(n):
    st = ipt()
    left, right = 0, len(st)-2
    diff = 0
    
    while left <= right:
        if st[left] != st[right]:
            diff += 1
        left += 1
        right -= 1
    print(diff)
