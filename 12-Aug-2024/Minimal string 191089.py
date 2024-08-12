# Problem: Minimal string - https://codeforces.com/contest/797/problem/C

from collections import defaultdict

s = input()
t = []
u = []

chars_count = defaultdict(int)
chars = [chr(i) for i in range(97, 123)]
char_index = 0

for ch in s:
    chars_count[ch] += 1

for index, ch in enumerate(chars):
    if chars_count[ch] > 0:
        char_index = index
        break

for char in s:
    t.append(char)
    chars_count[char] -= 1

    while char_index < 25 and chars_count[chars[char_index]] == 0:
        char_index += 1

    while t and t[-1] <= chars[char_index]:
        u.append(t.pop())

print(''.join(u + t[::-1]))
