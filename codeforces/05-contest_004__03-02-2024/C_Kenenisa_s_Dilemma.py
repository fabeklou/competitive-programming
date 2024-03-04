n = int(input())
arr = [int(c) for c in input().split()]
perm = 0
perm_idx = []

for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if arr[min_index] > arr[j]:
            min_index = j
    if min_index != i:
        perm += 1
        arr[i], arr[min_index] = arr[min_index], arr[i]
        perm_idx.append((i, min_index))

print(perm)
for i in range(perm):
    # print(" ".join(map(str, perm_idx[i])))
    print(*perm_idx[i])
