N, K = map(int, input().split())

arr = [0] * N
for i in range(N):
    arr[i] = int(input())
arr.sort()

L = 0
stones = curr = 0

for R in range(1, N):
    if L != R and arr[R] - arr[L] <= K:
        curr = R-L+1
        if R == N-1:
            stones += curr
    else:
        stones += curr
        curr = 0
        if L != R:
            L = R
print(stones)
