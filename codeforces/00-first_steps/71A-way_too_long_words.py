# Get the size of the total number of expected input
size = int(input())

for _ in range(size):
    st = input()
    st_len = len(st)
    # if <st_len>, the length of the string is greater than 10,
    # we will shorten it, otherwise we sill just print it
    if st_len > 10:
        print(f"{st[0]}{st_len-2}{st[-1]}")
    else:
        print(st)
