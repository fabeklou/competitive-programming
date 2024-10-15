from collections import defaultdict

n = int(input())
s = input()
# How many different Pokemons are there to capture ?
pokemons = len(set(s))

captured = defaultdict(int)
L = count = 0
mini = float("+inf")

for R in range(n):
    if s[R] not in captured:
        count += 1
    captured[s[R]] += 1
    if count == pokemons:
        while count == pokemons:
            mini = min(mini, R-L+1)
            captured[s[L]] -= 1
            if captured[s[L]] == 0:
                del captured[s[L]]
                count -= 1
            L += 1

print(0 if mini == float("+inf") else mini)
