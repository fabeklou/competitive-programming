# Get user input (melon size in kg) and convert it to integer.
size = int(input())

# The lowest even number greater than 0 is 2.
# For each one of the boys to have at least 2kg of melon
# the melon size need to be at least 4kg and even.
if size >= 4 and not size % 2:
    print('YES')
else:
    print('NO')
