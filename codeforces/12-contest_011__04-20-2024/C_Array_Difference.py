for _ in range(int(input())):
    n,m=map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    PS=B.copy()
    for i in range(1,m):
        PS[i]=B[i]+B[i-1]
    LA=LB=0
    RA=n-1
    RB=m-1
    # 1 2 4 6 
    # 7 5 3 3 2 1
    MAX=0
    while LA<=RA:
        if abs(A[LA]-B[RB]) > abs(A[RA]-B[LB]):
            MAX+=abs(A[LA]-B[RB])
            LA+=1
            RB-=1
        else:
            MAX+=abs(A[RA]-B[LB])
            LB+=1
            RA-=1
    print(MAX)
