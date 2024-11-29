# Problem:  Divisible Array - https://codeforces.com/contest/1828/problem/A

for _ in range(int(input())):
    n = int(input())
    result = [(index + 1) * 2 for index in range(n)]
    print(*result)
