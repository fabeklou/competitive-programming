import math

n, m, a = map(int, input().split())

def theatreSquare(n, m, a):
    return math.ceil(n/a) * math.ceil(m/a)

print(theatreSquare(n, m, a))
