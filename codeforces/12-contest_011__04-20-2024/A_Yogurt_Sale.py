for _ in range(int(input())):
    n,a,b = map(int, input().split())
    if a*2 >= b:
        if n % 2==1:
            print(n//2*b+a)
        else:
            print(n//2*b)
    else:
        print(n*a)
