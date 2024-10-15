import sys
from collections import Counter

ipt = sys.stdin.readline

n, m = map(int, ipt().split())
arr1, arr2 = map(int, ipt().split()), map(int, ipt().split())

hmap = Counter(arr1)
count = 0

for num in arr2:
    count += hmap.get(num, 0)

print(count)
