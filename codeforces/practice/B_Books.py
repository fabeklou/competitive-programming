import sys

ipt = sys.stdin.readline

n, t = map(int, ipt().split())
a = list(map(int, ipt().split()))

read_time = 0
book_count = 0
L = 0

for R in range(n):
    read_time += a[R]
    while read_time > t:
        read_time -= a[L]
        L += 1
    book_count = max(book_count, R-L+1)

print(book_count)
