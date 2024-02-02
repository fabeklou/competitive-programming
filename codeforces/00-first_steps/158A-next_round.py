# Get the user input containing the second input size
# and the index of the minimum score,
# then extract only the index and convert it into an integer.
k = int(input().split()[1])
# Get the input containing the scores and turns it
# into a list of integer score
scores = list(map(int, input().split()))

min_score = scores[k - 1]
nxt_rnd = 0
 
for score in scores:
    # If a score in the list is greater or equal to the minimum
    # to pass and not null then, one more contestant has passed
    if score >= min_score and score != 0:
        nxt_rnd += 1
    else:
        break
print(nxt_rnd)
