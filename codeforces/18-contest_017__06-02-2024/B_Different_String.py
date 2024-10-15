for _ in range(int(input())):
    string = input()
    if len(set(string)) == 1:
        print('NO')
    else:
        print('YES')
        splitted = list(string)
        sorted_splitted = sorted(splitted)
        if splitted == sorted_splitted:
            sorted_splitted = reversed(sorted_splitted)
        print(''.join(sorted_splitted))
