# Problem: E - World is Mine - https://codeforces.com/gym/536373/problem/E

import heapq
from collections import Counter

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    cakes_count = Counter(arr)

    cakes = [(k, v) for k, v in cakes_count.items()]
    cakes.sort()
    bob_count = 0
    bob_cakes = []

    for index in range(len(cakes)):
        bob_turn = bob_count + cakes[index][1]
        alice_turn = index - len(bob_cakes)
        bob_count += cakes[index][1]

        heapq.heappush(bob_cakes, -cakes[index][1])

        if bob_turn > alice_turn:
            bob_count += heapq.heappop(bob_cakes)

    print(len(cakes) - len(bob_cakes))
