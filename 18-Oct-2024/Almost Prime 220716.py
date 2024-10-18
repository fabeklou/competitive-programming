# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

n = int(input())
amount_of_almost_prime = 0

for num in range(2, n + 1):
    divided_by = 2
    divisors_count = set()
    while num > 1:
        if num % divided_by == 0:
            num //= divided_by
            divisors_count.add(divided_by)
        else:
            divided_by += 1
    if len(divisors_count) == 2:
        amount_of_almost_prime += 1
    divided_by, divisors_count = 2, set()

print(amount_of_almost_prime)
