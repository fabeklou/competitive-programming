for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    seen = set()
    find=False
    for i in range(n-2,-1,-1):
        if i == 0:
            val = a[0]
        else:
            val = a[i] - a[i-1]
        if val in seen:
            print("NO")
            find=True
            break
        seen.add(val)
        print(seen)
    if find:
        continue
    print("YES")
