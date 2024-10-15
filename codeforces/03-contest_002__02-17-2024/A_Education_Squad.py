board = []
individual_wins, team_wins = 0, 0

# getting inputs and create a string list representing the board
"""
[
    'ZOW',
    'YYO',
    'ABZ'
]
"""
for _ in range(3):
    s = input()
    board.append(s)

# find horizontal (row) wins
for str in board:
    unique = len(set(str))
    if unique == 1:
        individual_wins += 1
    if unique == 2:
        team_wins += 1

# find vertical (column) wins
for idx in range(3):
    x0, x1, x2 = board[0][idx], board[1][idx], board[2][idx]
    unique = len(set((x0, x1, x2)))
    if unique == 1:
        individual_wins += 1
    elif unique == 2:
        team_wins += 1

# find diagonal wins
y0, y1, y2 = board[0][0], board[1][1], board[2][2]
hset1_len = len(set((y0, y1, y2)))
if hset1_len == 1:
    individual_wins += 1
elif hset1_len == 2:
    team_wins += 1

z0, z1, z2 = board[0][2], board[1][1], board[2][0]
hset2_len = len(set((z0, z1, z2)))
if hset2_len == 2:
    team_wins += 1
elif hset2_len == 1:
    individual_wins += 1

print(individual_wins)
print(team_wins)
