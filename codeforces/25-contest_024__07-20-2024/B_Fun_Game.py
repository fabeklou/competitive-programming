for _ in range(int(input())):
    n = int(input())
    sequence = list(input())
    tequence = list(input())

    i = 0
    while i < n and sequence[i] == '0':
        if tequence[i] == '1':
            print('NO')
            break
        i += 1
    else:
        print('YES')
