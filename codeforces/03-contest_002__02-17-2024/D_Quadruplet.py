from collections import Counter

indexs = []
target, size = map(int, input().split())
rest = 0

str_nums = input().split()
int_nums = list(map(int, str_nums))
int_nums.sort()

# get count frequency of values in the list
hashmap = Counter(int_nums)

for num in int_nums:
    rest = target - num
    if rest <
    