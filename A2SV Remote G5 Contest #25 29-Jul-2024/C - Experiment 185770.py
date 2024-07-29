# Problem: C - Experiment - https://codeforces.com/gym/537575/problem/C

import heapq

exps = []
last_exp = first_exp = 0

for _ in range(int(input())):
    start, end, rooms = map(int, input().split())
    exps.append((start, end, rooms))
    last_exp = max(last_exp, start)
    first_exp = min(first_exp, start)

heapq.heapify(exps)
running_exps = []
max_rooms = 0
curr_rooms = 0

for time in range(first_exp, last_exp + 1):
    while exps and exps[0][0] == time:
        _, end, rooms = heapq.heappop(exps)
        heapq.heappush(running_exps, (end + 1, rooms))
        curr_rooms += rooms

    while running_exps and running_exps[0][0] == time:
        _, rooms = heapq.heappop(running_exps)
        curr_rooms -= rooms

    max_rooms = max(max_rooms, curr_rooms)

print(max_rooms)