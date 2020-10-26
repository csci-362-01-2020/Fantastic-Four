#!/bin/env python3

# import necessary libraries
import math
import sys

sys.path.append('../project/src/calculate-activity')

import functions as fun

def testAdd(operands):

    # invoke the add method for the functions.py file 
    test = fun.add(operands[0], operands[1])

    # return the result
    return test

    


