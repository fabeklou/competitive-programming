from collections import deque

n = int(input())

potions = list(map(int, input().split()))
max_drunk = 0

dq = deque([(0, 0, 0)])  # health, count, potion_index
while dq:
    h, count, index = dq.popleft()
    
    max_drunk = max(max_drunk, count)

    if index >= n:
        continue

    if potions[index] + h >= 0:
        dq.append((potions[index] + h, count + 1, index + 1))
        if potions[index] < 0:
            dq.append((h, count, index + 1))

print(max_drunk)
