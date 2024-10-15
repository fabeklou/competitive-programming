import sys

for _ in range(int(input())):
    rows, cols = map(int, input().split())
    maze = []
    for _ in range(rows):
        maze.append(list(input()))
    
    # find first good person index
    good_col, good_row = -1
    
    # find number of good persons
    good_count = 0
    
    
    if good_count == 0:
        print("NO")
        sys.exit()
