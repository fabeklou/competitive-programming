for _ in range(int(input())):
    n, k = map(int, input().split())
    potions_costs = [0] + list(map(int, input().split()))
    possessed_potions = set(map(int, input().split()))
    
    result = [0] * (n+1)
    for potion in range(1, n + 1):
        dependencies = [potion] + list(map(int, input().split()))
        if potion in possessed_potions:
            result.append(0)
            continue
        
    print(*result[1:])
