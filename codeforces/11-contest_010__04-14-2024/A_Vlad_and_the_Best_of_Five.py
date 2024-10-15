from collections import Counter

for _ in range(int(input())):
    S = input()
    count = Counter(S)
    if count['B'] > count['A']: print('B')
    else: print('A')
    