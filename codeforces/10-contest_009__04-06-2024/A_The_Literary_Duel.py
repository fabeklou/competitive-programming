n = int(input())
a = list(map(int, input().split()))

he=ha=0
L,R=0,n-1
turn=True
while L<=R:
    if turn:
        if a[R]>a[L]:
            he+=a[R]
            R-=1
        else:
            he+=a[L]
            L+=1
        turn=False
    else:
        if a[R]>a[L]:
            ha+=a[R]
            R-=1
        else:
            ha+=a[L]
            L+=1
        turn=True
        
print(he,ha)
