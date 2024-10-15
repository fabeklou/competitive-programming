for _ in range(int(input())):
    string = input()
    a_count = 0
    for char in string:
        if char == 'A':
            a_count += 1
    if a_count > 2:
        print('A')
    else:
        print('B')
