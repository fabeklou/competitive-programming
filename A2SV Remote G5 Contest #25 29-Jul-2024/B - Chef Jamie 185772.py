# Problem: B - Chef Jamie - https://codeforces.com/gym/537575/problem/B

n = int(input())
fruits = list(map(int, input().split()))
sorted_fruits = sorted(fruits)

left_index = 0
right_index = n-1

for index in range(len(fruits)):
    if fruits[index] != sorted_fruits[index]:
        left_index = index
        break

for index in range(len(fruits) - 1, -1, -1):
    if fruits[index] != sorted_fruits[index]:
        right_index = index
        break

if left_index >= right_index:
    print(0)
else:
    unique_fruits = set(fruits[left_index:right_index + 1])
    print(len(unique_fruits) - 1)
