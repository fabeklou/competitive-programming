# Problem: Grading Students - https://www.hackerrank.com/challenges/grading/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    result = []
    for grade in grades:
        last_digit = grade % 10
        if grade < 38:
            result.append(grade)
        elif last_digit > 7:
            result.append(grade + (10 - last_digit))
        elif 3 <= last_digit <= 5:
            result.append(grade + (5 - last_digit))
        else:
            result.append(grade)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
