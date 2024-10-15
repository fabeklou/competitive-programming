import heapq

n, k = map(int, input().split())
l_b = []

for _ in range(n):
    x, y = map(int, input().split())
    l_b.append((x, y))

l_b.sort(key=lambda x: x[1], reverse=True)

heap = []
max_pleasure = 0
sum_length = 0

for l, b in l_b:
    sum_length += l
    heapq.heappush(heap, l)

    if len(heap) > k:
        sum_length -= heapq.heappop(heap)

    max_pleasure = max(max_pleasure, sum_length * b)

print(max_pleasure)

