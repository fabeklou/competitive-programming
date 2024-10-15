from collections import deque

for _  in range(int(input())):
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))


    def inbound(row, col):
        return 0 <= row < n and 0 <= col < m


    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    largest_lake = 0
    for row in range(n):
        for col in range(m):
            if matrix[row][col] > 0:
                lake_volume = 0
                dq = deque([(row, col)])
                lake_volume += matrix[row][col]
                matrix[row][col] = 0

                while dq:
                    curr_row, curr_col = dq.popleft()

                    for r, c in directions:
                        new_row, new_col = curr_row + r, curr_col + c
                        if inbound(new_row, new_col) and matrix[new_row][new_col] > 0:
                            dq.append((new_row, new_col))
                            lake_volume += matrix[new_row][new_col]
                            matrix[new_row][new_col] = 0

                largest_lake = max(largest_lake, lake_volume)

    print(largest_lake)
