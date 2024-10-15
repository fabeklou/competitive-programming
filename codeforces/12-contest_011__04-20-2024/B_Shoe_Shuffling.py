from collections import Counter

for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    
    if len(set(A))==1:
        print(*[N]+[i for i in range(1, N)])
    else:
        print(-1)
