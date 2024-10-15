from collections import deque

for _ in range(int(input())):
    n, k = map(int, input().split())
    dq = deque(map(int, input().split()))

    left_attacks = 0
    right_attacks = 0
    if k % 2 == 0:
        left_attacks = k // 2
        right_attacks = k // 2
    else:
        left_attacks = k // 2 + 1
        right_attacks = k // 2

    while dq and (left_attacks > 0 or right_attacks > 0):
        # left attack
        if left_attacks >= dq[0]:
            left_attacks -= dq[0]
            dq.popleft()
        else:
            dq[0] -= left_attacks
            left_attacks = 0

        # right attack
        if dq and right_attacks >= dq[-1]:
            right_attacks -= dq[-1]
            dq.pop()
        elif dq and right_attacks < dq[-1]:
            dq[-1] -= right_attacks
            right_attacks = 0

    print(n - len(dq))
