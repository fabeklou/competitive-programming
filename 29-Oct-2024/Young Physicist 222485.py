# Problem: Young Physicist - https://codeforces.com/problemset/problem/69/A

x = y = z = 0
for _ in range(int(input())):
    a, b, c = map(int, input().split(' '))
    x += a
    y += b
    z += c
print('YES' if x == y == z == 0 else 'NO')
