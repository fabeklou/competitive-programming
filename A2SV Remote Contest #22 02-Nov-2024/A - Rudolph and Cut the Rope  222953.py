# Problem: A - Rudolph and Cut the Rope  - https://codeforces.com/gym/533316/problem/A

for _ in range(int(input())):
    n = int(input())
    a = []
    for _ in range(n):
        x, y = map(int, input().split())
        a.append(x - y)
    a.sort(reverse=True)
    res = 0
    for index in range(len(a)):
        if a[index] <= 0:
            break
        res += 1
    print(res)
