import sys

ipt = sys.stdin.readline
n, s = map(int, ipt().split())
arr = list(map(int, ipt().split()))

curr_sum = curr_len = maxi_len = 0
L = 0

for R in range(0, n):
    curr_sum += arr[R]
    curr_len += 1

    while curr_sum > s:
        curr_sum -= arr[L]
        curr_len -= 1
        L += 1

    maxi_len = max(maxi_len, curr_len)

print(maxi_len)
