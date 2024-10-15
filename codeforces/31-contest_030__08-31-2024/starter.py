tests = int(input())
for _ in range(tests):
    x = int(input())
    minimum_number = x & -x
    while True:
        if (x & minimum_number) and (x ^ minimum_number):
            break
        minimum_number += 1
    print(minimum_number)
