#!/bin/env python3

# import necessary libraries
import math
import sys

def testDiv(operands):

    sys.path.append('project/src/calculate-activity')

    import functions as fun

    # invoke the div method for the functions.py file
    test = fun.div(operands[0], operands[1])

    # return the result
    return test
