from collections import defaultdict

for _ in range(int(input())):
    N=int(input())
    S=input()
    COUNT = defaultdict(int)
    GOOD=0
    L=0
    for R in range(N):
        COUNT[S[R]]+=1
        GOOD+=COUNT[S[R]]
    print(GOOD)
