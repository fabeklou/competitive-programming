for _ in range(int(input())):
    """
    Simulation:
        3
            660(330)   8
            10 6 11
        4
            221(110)    16
            13 17 1 1
        5
            12(6)      32
            1 1 12 1 1
        6
            529200(264600)      64
            20 7 14 18 3 5
    """
    N = int(input())
    nums = list(map(int, input().split()))
    DIV = 2**N
    ops=1

    _prod = 1
    for num in nums:
        _prod *= num

    if _prod % DIV == 0:
        print(0)
        continue
    
    nums.sort()
    
    for idx, num in enumerate(nums):
        if idx == 0: continue
        _prod *= (idx+1)
        if _prod % DIV == 0:
            print(ops)
            break
        ops+=1
        
    else:
        print(-1)
