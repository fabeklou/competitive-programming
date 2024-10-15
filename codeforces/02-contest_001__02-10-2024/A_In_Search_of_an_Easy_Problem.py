n = int(input())
l = input()  # '1 0 0 1'

if l[-1] == 0 or '1' in l:
    print('HARD')
else:
    print('EASY')
