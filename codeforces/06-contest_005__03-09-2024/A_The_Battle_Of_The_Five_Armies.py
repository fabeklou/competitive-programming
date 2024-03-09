import sys
from collections import defaultdict, Counter, deque
ipt = sys.stdin.readline
power = list(map(int, ipt().split()))
number = list(map(int, ipt().split()))

bilbo, enemy = 0, 0
for i in range(len(power)):
    if i <= 2:
        bilbo += power[i] * number[i]
    else:
        enemy += power[i] * number[i]
if enemy == bilbo:
    print("DRAW")
elif bilbo > enemy:
    print("WIN")
else:
    print("LOSE")
