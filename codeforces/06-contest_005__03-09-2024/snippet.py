# Essential module to import
import sys
from collections import defaultdict, Counter, deque
from itertools import zip_longest

# Frequently used instructions
ipt = sys.stdin.readline

# get single input (int):
n = int(ipt())

# get an integer list
l = list(map(int, ipt().split()))

# get an integer map object to iterate over:
l = map(int, ipt().split())

# iterate over multiple iterable in parallel:
for x, y in zip_longest(l1, l2, fillvalue=None):

# iterate over multiple iterable in parallel and get index:
for index, values in enumerate(zip_longest(l1, l2, fillvalue=None)):
    val1, val2 = values


import sys
from collections import defaultdict, Counter, deque
from itertools import zip_longest


ipt = sys.stdin.readline
n = int(ipt())
l = list(map(int, ipt().split()))
l = map(int, ipt().split())
for x, y in zip_longest(l1, l2, fillvalue=None):
    pass
for index, values in enumerate(zip_longest(l1, l2, fillvalue=None)):
    val1, val2 = values
