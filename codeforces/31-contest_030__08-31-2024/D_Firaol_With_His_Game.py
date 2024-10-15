for _ in range(int(input())):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))

    total_time = 0
    max_challenge = -1
    skip_index = -1

    for i in range(n):
        total_time += a[i]
        if a[i] > max_challenge:
            max_challenge = a[i]
            skip_index = i + 1

        if total_time > s:
            break

    if total_time <= s:
        print(0)
        continue

    total_time_with_skip = total_time - max_challenge

    if total_time_with_skip <= s:
        print(skip_index)
    else:
        print(0)
