# Problem: A - Maximum Multiple Sum - https://codeforces.com/gym/559568/problem/A

for _ in range(int(input())):
    n =  int(input())
    result = 2
    sm = 2
    for val1 in range(2, n + 1):
        curr = 0
        for val2 in range(val1, n + 1, val1):
            curr += val2
        if curr > sm:
            result, sm = val1, curr
    print(result)
