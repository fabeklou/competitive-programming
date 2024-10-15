N,M=map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
MAX=float('-inf')
J=0
for I in range(N):
    while J<M-1 and abs(A[I]-B[J+1])<=abs(A[I]-B[J]):
        J+=1
    MAX=max(MAX, abs(A[I]-B[J]))
print(MAX)
