#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # 1 << 32 places 1 at 1st postion followed by 32 zeros (making it 33 bits)
    #however, -1 will make it to 32 bit integer will all 1 (i.e. 2**32)
    # - n will remove the bits which are in the numbers hence we have flipped bits.
    return (1 << 32) - 1 - n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
