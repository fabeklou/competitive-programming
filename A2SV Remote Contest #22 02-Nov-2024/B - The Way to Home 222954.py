# Problem: B - The Way to Home - https://codeforces.com/gym/533316/problem/B

n, d = map(int, input().split())
s = input()

pos = 0
jumps = 0
can_reach = True

while pos != n - 1:
    next_pos = -1
    for i in range(pos + 1, min(pos + d + 1, n)):
        if s[i] == '1':
            next_pos = i
    if next_pos == -1:
        can_reach = False
        break
    pos = next_pos
    jumps += 1

print(jumps if can_reach else -1)
