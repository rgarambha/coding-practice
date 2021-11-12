#!/bin/python3

import math
import os
import random
import re
import sys
# import numpy as np
#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positive_count = 0
    negative_count = 0
    zero_count = 0
    for i in arr:
        if i > 0:
            positive_count +=1
        elif i<0:
            negative_count += 1
        else:
            zero_count +=1
    
            
    ### numpy implementation
    # arr = np.array(arr)
    # positive_count = np.count_nonzero(arr > 0)
    # negative_count = np.count_nonzero(arr < 0)
    # zero_count = np.count_nonzero(arr == 0)
            
            
            
    total_count = len(arr)
    print( '{:.6f}'.format(round(positive_count/total_count, 6)))
    print( '{:.6f}'.format(round(negative_count/total_count, 6)))
    print( '{:.6f}'.format(round(zero_count/total_count, 6)))
    
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
