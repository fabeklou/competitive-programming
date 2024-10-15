from collections import defaultdict
from itertools import combinations

n, m = map(int, input().split())
names = []
conflicts = set()

for _ in range(n):
    names.append(input())

for _ in range(m):
    name1, name2 = input().split()
    conflicts.add((name1, name2))
    conflicts.add((name2, name1))

for size in range(n, 0, -1):
    for combination in combinations(names, size):
        team_is_valid = True

        for i in range(len(combination)):
            for j in range(i + 1, len(combination)):
                if (combination[i], combination[j]) in conflicts:
                    team_is_valid = False
                    break

            if not team_is_valid:
                break

        if team_is_valid:
            print(len(combination))
            for name in sorted(combination):
                print(name)
            exit()
