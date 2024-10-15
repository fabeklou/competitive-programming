from heapq import heapify, heappop, heappush

n = int(input())
h = []

for _ in range(n):
    args = input().split()

    if len(args) == 1:
        if h:
            heappop(h)
        else:
            print(f"insert {1}")
    elif args[0] == 'insert':
        value = args[1]
        heappush(h, value)
    else:
        value = args[1]
        while h and h[0] < value:
            heappop(h)
            print('removeMin')
        if not h or h[0] != value:
            heappush(h, value)
            print(f'insert {value}')
        print(f'getMin {value}')
