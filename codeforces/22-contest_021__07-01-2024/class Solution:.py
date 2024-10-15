class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        rows = len(board)
        reverse = 1

        oneD = [-1]
        for row in range(rows-1, -1, -1):
            oneD += board[row][::reverse]
            reverse = 1 if reverse == -1 else -1
        print(oneD)
        destination = len(oneD) - 1
        dq = deque([(1, 0)])
        visited = set([1])

        while dq:
            posi, ope = dq.popleft()
            # print(f'Position: {posi}, Moves: {ope}')
            if posi == destination:
                return ope

            for di in range(1, 7):
                new_pos = posi + di
                # print(f"new position: {new_pos}")
                if new_pos <= destination and new_pos not in visited:
                    if oneD[new_pos] != -1:
                        new_pos = oneD[new_pos]
                    if new_pos not in visited:
                        dq.append((new_pos, ope+1))
                        visited.add(new_pos)

        return -1
