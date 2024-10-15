from collections import Counter

mapping = {chr(i): i - ord('A') + 1 for i in range(ord('A'), ord('Z')+1)}

for _ in range(int(input())):
    N = int(input())
    count = Counter(input())
    num=0
    for key, value in count.items():
        if mapping[key] <= value:
            num+=1
    print(num)
