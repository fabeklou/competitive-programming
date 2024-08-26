# Problem: A - Maximum Increase - https://codeforces.com/gym/543262/problem/A

n = int(input())
a = list(map(int, input().split()))

maxi = 0
curr = 0
for i in range(0, n-1):
    if a[i] < a[i+1]:
        curr += 1
    else:
        curr = 0
    maxi = max(maxi, curr)

print(maxi+1)
