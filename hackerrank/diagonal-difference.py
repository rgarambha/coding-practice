#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    n = len(arr)
    m = len(arr[0])
    sum_diag1, sum_diag2 = 0 , 0
    for i in range(n):
        for j in range(m):
            if i == j:
                sum_diag1 += arr[i][j]
            if i+j+1 == n:
                sum_diag2 += arr[i][j]
                
    return abs(sum_diag1 - sum_diag2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
