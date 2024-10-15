import sys

ipt = sys.stdin.readline

t = int(ipt())

# We are looking for the longuest valid subarray first
# and then we can calculate and print the number of
# suitable pairs of indices for that subarray.

for _ in range(t):
    n = int(ipt())
    a = list(map(int, ipt().split()))
    curr_count = max_count = 0
    L = 0
    for R in range(n):
        if R == 0 and a[R] >:
        
        max_count += ((curr_count * (curr_count+1))//2)
    print(max_count)
