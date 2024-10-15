from collections import deque

word = input()
expected = deque(['h', 'e', 'l', 'l', 'o'])

for char in word:
    if char == expected[0]:
        expected.popleft()
        if not expected:
            break

print("YES" if not expected else "NO")

