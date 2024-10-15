def can_read(n_of_books, prefix_sum):
    """
    calcute the minimum time it will take to read n_of_books
    """
    size = len(prefix_sum)
    min_time = float('+inf')
    for i in range(n_of_books, size):
        min_time = min(min_time, prefix_sum[i] - prefix_sum[i - n_of_books])
    return min_time

#[4, 5]
#[3, 1, 2, 1]
num, minutes = map(int, input().split())
book_min = list(map(int, input().split()))

# calculate prefixSum of the book_min
# 3 1 2 1    ->   0 3 4 6 7
prefix_sum = [0]
for m in book_min:
    prefix_sum.append(m + prefix_sum[-1])

# reads no book if minutes < min(book_min)          : left
# or read all of them if minutes >= sum(book_min)   : right
left, right = 0, num
count = 0

while left <= right:
    mid = left + (right - left) // 2

    min_time = can_read(mid, prefix_sum)

    if min_time == minutes:
        count = mid
        break
    elif min_time < minutes:
        left = mid + 1
        count = max(count, mid)
    else:
        right = mid - 1

print(count)
