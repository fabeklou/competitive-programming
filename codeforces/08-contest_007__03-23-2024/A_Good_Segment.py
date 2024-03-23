n = int(input())
s = input()

L = 0
maxi = 1
for R in range(1, n):
    if ord(s[R]) == ord(s[R-1]) + 1:
        maxi = max(maxi, R-L+1)
    else:
        maxi = max(maxi, R-L)
        L = R
print(maxi)
