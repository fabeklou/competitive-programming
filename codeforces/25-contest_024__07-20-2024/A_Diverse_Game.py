for _ in range(int(input())):
    n, m = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]

    if n * m == 1:
        print(-1)
        continue

    for row in range(n):
        for col in range(m):
            if mat[row][col] == n * m:
                mat[row][col] = 1
            else:
                mat[row][col] +=1

    for r in mat:
        print(*r)
