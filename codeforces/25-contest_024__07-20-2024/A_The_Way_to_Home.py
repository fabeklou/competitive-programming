import sys

dist, jump = map(int, input().split())

route = input()

posi = 0
ops = 0

while posi < dist:
    next_posi = posi
    for i in range(1, jump + 1):
        if posi + i < dist and route[posi + i] == '1':
            next_posi = posi + i
        if next_posi == dist - 1:
            print(ops + 1)
            sys.exit()

    if next_posi == posi:
        print(-1)
        break

    ops += 1
    posi = next_posi
