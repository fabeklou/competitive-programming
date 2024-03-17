t = int(input())

os = "codeforces"

for _ in range(t):
    rs = input()
    size = len(rs)
    count = 0
    
    for i in range(size):
        if rs[i] != os[i]:
            count += 1
    print(count)