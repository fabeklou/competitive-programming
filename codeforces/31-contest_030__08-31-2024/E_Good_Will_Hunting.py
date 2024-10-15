l, r = map(int, input().split())

xor = l ^ r
msb = 1
while xor:
    msb <<= 1
    xor >>= 1
print(msb - 1)
