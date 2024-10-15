n = int(input())
a = map(int, input().split())

dct = {}

# [2, 3, 4, 4]  -> 2
for size in a:
    if size not in dct:
        dct[size] = 1
    else:
        dct[size] += 1

print(max(dct.values()))
