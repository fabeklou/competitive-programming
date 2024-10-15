n, m = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

result = []
j = 0

for i in range(m):
    while j < n and arr1[j] < arr2[i]:
        j += 1
    result.append(j)

print(*result)
