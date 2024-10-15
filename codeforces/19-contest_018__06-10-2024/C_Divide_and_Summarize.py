t = int(input())

# https://codeforces.com/gym/528793/problem/C

def rec(array):
    if not array:
        return
    
    valid_sums.add(sum(array))

    mid = (max(array) + min(array)) // 2
    left = [value for value in array if value <= mid]
    right = [value for value in array if value > mid]

    rec(left)
    rec(right)


for _ in range(t):
    n, q = map(int, input().split())

    array = list(map(int, input().split()))
    p_tests = [int(input()) for _ in range(q)]
    
    array.sort()
    valid_sums = set()

    rec(array)

    for test in p_tests:
        if test in valid_sums:
            print('YES')
        else:
            print('NO')
