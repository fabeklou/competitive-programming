
for _ in range(int(input())):
    a, b = map(int, input().split())
    teams = min(min(a, b), (a + b) // 4)
    print(teams)
