n, m = map(int, input().split())

rows = []

for _ in range(n):
    row = list(input())
    if len(set(row)) > 1 or (rows and rows[-1] == row[0]):
        print("NO")
        break
    rows.append(row[0])
else:
    print("YES")
