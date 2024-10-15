import sys

ipt = sys.stdin.readline

for _ in range(int(ipt())):
    N = int(ipt())
    A = list(map(int, ipt().split()))
    found=False

    for I in range(N-1):
        IDX=I
        for J in range(I+1, N):
            if (A[I] + A[J])%2==0 and A[J]<A[IDX]:
                IDX=J
        if IDX!=I:
            A[IDX],A[I]=A[I],A[IDX]
        if I>0 and A[I] < A[I-1]:
            print('NO')
            found=True
            break
    if not found:
        print('YES' if A[N-1]>=A[N-2]  else 'NO')
