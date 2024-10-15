import sys

ipt = sys.stdin.readline

for _ in range(int(ipt())):
    N,X,Y=map(int, ipt().split())
    A=list(map(int, ipt().split()))
    COUNT=0
    for I in range(N-1):
        for J in range(I+1, N):
            if (A[I]+A[J])%X==0 and (A[I]-A[J])%Y==0:
                COUNT+=1
    print(COUNT)
