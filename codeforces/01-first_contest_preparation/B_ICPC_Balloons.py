t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    b = 0
    for i in range(len(s)):
        if s[i] in s[:i]:
            b += 1
        else:
            b += 2
    print(b)
