for _ in range(int(input())):
    string = input()
    list_string = []
    prev_cut = 0
    # find groups
    for idx in range(len(string)):
        if idx > 0 and string[idx] == '0' and string[idx-1] == '1':
            list_string.append(string[prev_cut:idx])
            prev_cut = idx
    list_string.append(string[prev_cut:len(string)])
    # find all '0...1' sequences
    count = 0
    for s in list_string:
        if len(s) > 1 and s[0] != s[-1]: count += 1
    # print(list_string, count)
    count = count - 1 if count > 0 else count
    print(len(list_string) + count)
