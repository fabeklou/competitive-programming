import heapq

for _ in range(int(input())):
    n = int(input())
    cards = list(map(int, input().split()))

    heap = []
    total_power = 0

    for card in cards:
        if card == 0:
            if heap:
                total_power += -heapq.heappop(heap)
        else:
            heapq.heappush(heap, -card)

    print(total_power)
