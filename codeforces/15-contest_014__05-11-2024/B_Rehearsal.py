arr = []

for _ in range(int(input())):
    arr.append(list(map(int, input().split())))

# sorted by preficiency
arr.sort(key=lambda x: x[1])

left, right = 0, len(arr)-1
min_time = float('-inf')

# [ (1, 2) (2, 5) (1, 8) ]
# [ (number, proficiency) ]
while left <= right:
    min_time = max(min_time, arr[left][1] + arr[right][1])
    diff = min(arr[left][0], arr[right][0])

    if left == right:
        break

    arr[left][0] -= diff
    arr[right][0] -= diff

    if arr[left][0] == 0:
        left += 1
    if arr[right][0] == 0:
        right -= 1

print(min_time)


# cmds = []
# size = 0

# for _ in range(int(input())):
#     x, y = map(int, input().split())
#     cmds.append((x, y))
#     size+=x

# arr = [0] * size
# idx = 0
# for x, y in cmds:
#     for _ in range(x):
#         arr[idx] = y
#         idx += 1

# arr.sort()
# left, right = 0, len(arr)-1
# min_time = float('-inf')

# while left < right:
#     min_time = max(min_time, arr[left] + arr[right])
#     left+=1
#     right-=1

# print(min_time)
