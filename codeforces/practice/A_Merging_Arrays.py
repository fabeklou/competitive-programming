import sys

ipt = sys.stdin.readline

n, m = map(int, ipt().split())
l1 = list(map(int, ipt().split()))
l2 = list(map(int, ipt().split()))

merged = []
i, j = 0, 0

while i < n or j < m:
    if i == n:
        merged.extend(l2[j:])
        break
    if j == m:
        merged.extend(l1[i:])
        break

    if l1[i] <= l2[j]:
        merged.append(l1[i])
        i += 1
    else:
        merged.append(l2[j])
        j += 1

print(*merged)
