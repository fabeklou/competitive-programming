for _ in range(int(input())):
    size = input()
    nums = list(map(int, input().split()))
    nums_sorted = sorted(nums)
    for num1, num2 in zip(nums, nums_sorted):
        if (num1 + num2) % 2 != 0:
            print('NO')
            break
    else:
        print('YES')
