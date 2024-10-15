from itertools import zip_longest

n = input()
m = input()

wrong = "WRONG_ANSWER"
good = "OK"

result = list(n)
result.sort()
size = len(result)

# find te first non zero and swapp it with the first zero:
for i in range(size):
    if result[i] != '0':
        result[0], result[i] = result[i], result[0]
        break

for left, right in zip_longest(result, m, fillvalue=None):
    if left != right:
        print(wrong)
        break
else:
    print(good)
