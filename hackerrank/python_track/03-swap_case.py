def swap_case(s):
    revert = ''
    for c in s:
        c_code = ord(c)
        if 65 <= c_code <= 90:
            revert += chr(c_code + 32)
        elif 97 <= c_code <= 122:
            revert += chr(c_code - 32)
        else:
            revert += c
    return revert
            

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
