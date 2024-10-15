from collections import defaultdict

N,M = map(int, input().split())
arr = list(map(int, input().split()))
count = defaultdict(int)
count[0] = 1
runnSum = good = 0
for num in arr:
    runnSum+=num
    div=runnSum%M
    good+=count[div]
    count[div]+=1
print(good)
