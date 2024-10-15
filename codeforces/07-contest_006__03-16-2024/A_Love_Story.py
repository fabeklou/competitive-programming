t = int(input())

os = "codeforces"

for _ in range(t):
    rs = input()
    count = 0

    for i in range(10):
        if rs[i] != os[i]:
            count += 1
    print(count)
