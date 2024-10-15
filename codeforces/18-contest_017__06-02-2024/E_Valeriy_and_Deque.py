from collections import deque
import sys

n, q = map(int, input().split())
dq = deque(map(int, input().split()))

if q == 0:
    sys.exit()

q_sizes = [int(input()) for _ in range(q)]
q_sizes.reverse()

q_max = max(dq)
eq_ops = 0

for ops in range(1, q_sizes[0] + 1):
    if ops == q_sizes[-1]:
        q_sizes.pop()
        print(dq[0], dq[1])
    if dq[0] > dq[1]:
        dq[0], dq[1] = dq[1], dq[0]
    dq.append(dq.popleft())

    if q_max == dq[0]:
        eq_ops = ops
        break

# eq_ops = 5
# [5,1,2,3,4]
max_value = dq.popleft()  # [1,2,3,4]
while q_sizes:
    querry = q_sizes.pop()

    print(max_value, )


# from collections import deque
# import sys

# n, q = map(int, input().split())
# dq = deque(map(int, input().split()))
# q_sizes = [int(input()) for _ in range(q)]
# q_sizes.sort(reverse=True)

# if len(q_sizes) == 0:
#     sys.exit()

# for ops in range(1, q_sizes[0] + 1):
#     if ops == q_sizes[-1]:
#         q_sizes.pop()
#         print(dq[0], dq[1])
#     if dq[0] > dq[1]:
#         dq[0], dq[1] = dq[1], dq[0]
#     dq.append(dq.popleft())
