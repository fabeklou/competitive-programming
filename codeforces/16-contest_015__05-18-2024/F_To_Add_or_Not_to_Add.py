
n, k = map(int, input().split())
a = list(map(int, input().split()))

# prefixSum and binary search
a.sort(reverse=True)
ps = [0]

for i in range(len(a)-1):
    ps.append(a[i] - a[i+1])

# binary search to find the max num of occurences

