#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hh = int(s[:2])
    mod_val = 24
    
    if "PM" in s:
        hh += 12 if hh != 12 else 0
    else:
        mod_val = 12
    return "{:02d}{}".format(hh%mod_val, s[2:-2])
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
