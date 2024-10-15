N,X = map(int, input().split())

arr = list(map(int, input().split()))
count=1
runnSum=0

for num in arr:
    runnSum+=num
    if runnSum>X:
        break
    count+=1
print(count)
