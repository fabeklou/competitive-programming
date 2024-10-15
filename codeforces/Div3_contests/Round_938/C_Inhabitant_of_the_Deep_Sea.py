import sys

ipt = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    L = 0
    R = n-1
    while L <= R and k > 0:
        MINI = a[R] if L == R else min(a[R], a[L], max(k//2, 1))
        print(f"""L: {L}, R: {R}, MINI: {MINI}, k: {
              k}, count: {count}, ARRAY: {a}""")
        a[R] -= MINI
        k -= MINI
        if k >= MINI and L < R:
            a[L] -= MINI
            k -= MINI

        if a[R] == 0:
            R -= 1
            count += 1
        if a[L] == 0 and L < R:
            L += 1
            count += 1
        print(f"""L: {L}, R: {R}, MINI: {MINI}, k: {
              k}, count: {count}, ARRAY: {a}""")

    print(count)
