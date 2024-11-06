# Problem: Counting Valleys - https://www.hackerrank.com/challenges/counting-valleys/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    rep = [0]
    result = 0
    for chr in path:
        if chr == "U":
            rep.append(rep[-1] + 1)
        else:
            rep.append(rep[-1] - 1)
    for index in range(len(rep) - 1):
        if rep[index] == 0 and rep[index + 1] < 0:
            result += 1
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
