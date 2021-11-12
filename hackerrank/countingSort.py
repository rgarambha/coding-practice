#!/bin/python3

import math
import os
import random
import re
import sys



# Comparison Sorting
# Quicksort usually has a running time of n log(n), but is there an algorithm
# that can sort even faster? In general, this is not possible. Most sorting 
# algorithms are comparison sorts, i.e. they sort a list just by comparing the
#  elements to one another. A comparison sort algorithm cannot beat n log(n)
#  (worst-case) running time, since n log(n) represents the minimum number of
#  comparisons needed to know where to place each element. 

# Alternative Sorting
# Another sorting method, the counting sort, does not require comparison. 
# Instead, you create an integer array whose index range covers the entire
#  range of values in your array to sort. Each time a value occurs in the
#  original array, you increment the counter at that index. At the end, 
# run through your counting array, printing the value of each non-zero 
# valued index that number of times.


#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    counts = [0 for i in range(100)]
    
    for i in arr:
        counts[i] += 1
    return counts

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
