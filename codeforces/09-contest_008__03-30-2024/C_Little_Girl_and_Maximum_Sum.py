n,q = map(int, input().split())

arr = list(map(int, input().split()))

queries = [list(map(int, input().split())) for _ in range(q)]

arr.sort(reverse=True)
prefixSum = []
runnSum=0
# calculate prefixSum
for num in arr:
    runnSum+=num
    prefixSum.append(runnSum)

# find min and max
mini = float("+inf")
# maxi = float("-inf")
for li, ri in queries:
    mini = min(li, mini)

# alter the request list
for i in range(q):
    queries[i][0]-=mini
    queries[i][1]-=mini

count=0
for li, ri in queries:
    if li == 0:
        count+=prefixSum[ri]
    else:
        count+=prefixSum[ri]-prefixSum[li-1]

print(arr)
print(queries)
print(count)
        