size = int(input())

# Total number of problems the friends
# will implement on the contest
count = 0

for _ in range(size):
    # If there are at least two <1> in the input line
    # then, the team can implement one more solution
    if input().count('1') > 1:
        count += 1

print(count)
