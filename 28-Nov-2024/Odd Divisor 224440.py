# Problem: Odd Divisor - https://codeforces.com/problemset/problem/1475/A

for _ in range(int(input())):
    num = int(input())
    result = False
    div = num
    while div > 1:
        if div % 2 == 1 and num % div == 0:
            result = True
            break
        div //= 2
    print("YES" if result else "NO")
