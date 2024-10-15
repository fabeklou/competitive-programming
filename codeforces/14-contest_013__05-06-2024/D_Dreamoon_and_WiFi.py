from collections import deque

s1 = input()
s2 = input()

pos1 = 0
for c in s1:
    pos1 = pos1 + (-1 if c == '-' else +1)

N = len(s2)
dq = deque([(0, -1)])
possibilities = 0
success = 0

while dq:
    pos2, idx = dq.popleft()
    
    if idx == N-1:
        possibilities += 1
        if pos2 == pos1: success += 1
    
    if idx < N-1:
        if s2[idx+1] == '+':
            dq.append((pos2+1, idx+1))
        elif s2[idx+1] == '-':
            dq.append((pos2-1, idx+1))
        else:
            dq.append((pos2+1, idx+1))
            dq.append((pos2-1, idx+1))

print(success / possibilities)
# print(F"{success / possibilities:24f}")
