import sys
ipt = sys.stdin.readline
st = ipt()

ptr, cons, max_cons = 0, 0, 0

for chr in st:
    if chr == 'O':
        cons += 1
        max_cons = max(cons, max_cons)
    else:
        cons = 0

print(max_cons)
