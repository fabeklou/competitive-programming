n, m  = map(int, input().split())

l = map(int, input().split())
s = {}

for dif in l:
    if not dif in s:
        s[dif] = 1
    else:
        s[dif] += 1

    if len(s) == n:
        print(1, end='')
        for i in range(1, n+1):
            s[i] -= 1
            if s[i] == 0:
                del s[i]
    else:
        print(0, end='')
