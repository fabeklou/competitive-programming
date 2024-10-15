import copy

n,k=map(int, input().split())
h=list(map(int, input().split()))
count=float('+inf')
index=0
prefixSum = copy.deepcopy(h)
for i in range(1,n):
    prefixSum[i]+=prefixSum[i-1]
for i in range(n-k+1):
    if i == 0:
        curr = prefixSum[k-1]
    else:
        curr = prefixSum[i+k-1] - prefixSum[i-1]
    # print(i, i-1, i+k-1, curr)
    if curr < count:
        index=i
        count=curr
print(index+1 if index != float("+inf") else 0)
