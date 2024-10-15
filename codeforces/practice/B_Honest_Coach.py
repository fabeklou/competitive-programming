t = int(input())

for _ in range(t):
    size = input()
    arr = sorted(map(int, input().split()))
    
    # if (size == '2'):
    #     print(abs(arr[0] - arr[1]))
    # else:
    #     print(min(abs(arr[0] - arr[1]), abs(arr[1] - arr[2])))

    prev = arr[0]
    jmp = float('inf')

    for item in arr[1:]:
        new_jmp = abs(item - prev)
        if new_jmp < jmp:
            jmp = new_jmp
        prev = item

    print(jmp)
