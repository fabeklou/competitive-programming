from collections import deque

n = int(input())
rots = [int(input()) for _ in range(n)]

dq = deque([[0, 0]])

while dq:
    value, index = dq.popleft()
    next_index = index + 1

    dq.append([(value + rots[index]) % 360, next_index])
    dq.append([(value - rots[index]) % 360, next_index])

    if dq[0][1] == len(rots):
        break


for value, _ in dq:
    if value == 0:
        print("YES")
        break
else:
    print('NO')
