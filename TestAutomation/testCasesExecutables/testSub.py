#!/bin/env python3

# import necessary libraries
import math
import sys

sys.path.append('../project/src/calculate-activity')

import functions as fun

def testSub(operands):

    # invoke the sub method for the functions.py file 
    test = fun.sub(operands[0], operands[1])

    # return the result
    return test
