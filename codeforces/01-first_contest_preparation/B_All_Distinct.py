t = int(input())

for _ in range(t):
    size = int(input())
    lst_str = input()

    list_int = [int(item) for item in lst_str.split()]
    unique = set(list_int)

    unique_len = len(unique)
    list_int_len = len(list_int)

    if unique_len % 2 == list_int_len % 2:
        print(unique_len)
    else:
        print(unique_len - 1)
