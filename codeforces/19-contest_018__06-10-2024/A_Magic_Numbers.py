num = input()
index = 0

while index < len(num):
    if num[index : index + 3] == '144':
        index += 3
    elif num[index : index + 2] == '14':
        index += 2
    elif num[index : index + 1] == '1':
        index += 1
    else:
        print('NO')
        break
else:
    print('YES')
