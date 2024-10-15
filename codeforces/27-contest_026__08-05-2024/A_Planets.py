from collections import Counter

for _ in range(int(input())):
    n, c = map(int, input().split())
    orbits = list(map(int, input().split()))
    
    count = 0
    uniq_orbit = Counter(orbits)
    for orbit, number in uniq_orbit.items():    
        count += min(c, number)

    print(count)
