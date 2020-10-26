#!/bin/env python3

# import necessary libraries
import math
import sys

sys.path.append('../project/src/calculate-activity')

import functions as fun

def testDiv(operands):

    # invoke the div method for the functions.py file
    test = fun.div(operands[0], operands[1])

    # return the result
    return test
