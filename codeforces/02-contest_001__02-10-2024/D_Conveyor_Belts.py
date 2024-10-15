t = int(input())
n, x1, y1, x2, y2 = map(int, input().split())

for _ in range(t):
    pad_1 = min(x1, y1, n - x1 + 1, n - y1 + 1)
    pad_2 = min(x2, y2, n - x2 + 1, n - y2 + 1)
    print(abs(pad_1 - pad_2))
