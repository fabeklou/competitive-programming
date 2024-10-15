t = int(input())

for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    if len(set(l)) == 1:
        print(l[0])
        continue
    print(l[-1] + l[-2] + l[-3] - (l[-1] - l[0]))
