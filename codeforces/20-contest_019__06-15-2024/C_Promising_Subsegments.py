from collections import Counter, defaultdict

for _ in range(int(input())):
    n, m, k = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    hMap = Counter(b)

    promising = 0
    left, right = 0, m - 1
    initialCount = defaultdict(int)
    initialCount.update(Counter(a[left: right + 1]))

    curr_count = 0
    for num in hMap:
        curr_count += min(hMap[num], initialCount[num])

    if curr_count >= k:
        promising += 1

    while right < n - 1:
        # Move window to the right by 1
        initialCount[a[left]] -= 1
        if initialCount[a[left]] < hMap[a[left]]:
            curr_count -= 1

        left += 1
        right += 1

        initialCount[a[right]] += 1
        if initialCount[a[right]] <= hMap[a[right]]:
            curr_count += 1

        if curr_count >= k:
            promising += 1

    print(promising)
