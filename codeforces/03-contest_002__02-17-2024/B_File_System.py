from collections import defaultdict

size = int(input())
hashmap = defaultdict(int)

for _ in range(size):
    path = input()
    if path in hashmap:
        print(f"{path}{hashmap[path]}")
    else:
        print('OK')
    hashmap[path] += 1
