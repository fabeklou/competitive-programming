N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

if N == K:
    print(A[K-1])
elif K == 0:
    print(A[0]-1 if A[0] > 1 else -1)
elif A[K-1] == A[K]:
    print(-1)
else:
    print(A[K-1])
