from collections import deque
n = int(input())
"""
0 1 2 3 4 5 6 7 8 Index
-----------------
1 2 3 4 5 6 7 8 9
9 2 3 4 5 6 7 8 1
2 9 3 4 5 6 7 8 1
2 3 9 4 5 6 7 8 1
2 3 4 9 5 6 7 8 1
2 3 4 5 9 6 7 8 1
2 3 4 5 6 9 7 8 1
2 3 4 5 6 7 9 8 1
2 3 4 5 6 7 8 9 1
2 3 4 5 6 7 8 1 9

"""
dq = deque()
for i in range(1, n+1):
    if i == n:
        dq.appendleft(i)
    else:
        dq.append(i)

print(*dq)
