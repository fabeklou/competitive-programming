#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    result = ''
    if (n % 2 == 1) or (6 <= n <= 20 and n % 2 == 0):
        result = 'Weird'
    else:
        result = 'Not Weird'
    print(result)
